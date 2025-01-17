from apps.system.models import Dept, User
from apps.system.serializers import UserSignatureSerializer, UserSimpleSerializer
from rest_framework import serializers
from apps.utils.serializers import CustomModelSerializer

from .models import State, Ticket, TicketFlow, Workflow, Transition, CustomField


class WorkflowSerializer(CustomModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'


class WorkflowCloneSerializer(CustomModelSerializer):
    class Meta:
        model = Workflow
        fields = ['name', 'key']


class StateSerializer(CustomModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class WorkflowSimpleSerializer(CustomModelSerializer):
    class Meta:
        model = Workflow
        fields = ['id', 'name', 'key']


class StateSimpleSerializer(CustomModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'type', 'distribute_type', 'enable_retreat', 'enable_deliver', 'key']


class TransitionSerializer(CustomModelSerializer):
    source_state_ = StateSimpleSerializer(source='source_state', read_only=True)
    destination_state_ = StateSimpleSerializer(source='destination_state', read_only=True)

    class Meta:
        model = Transition
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('source_state', 'destination_state')
        return queryset

class TransitionSimpleSerializer(CustomModelSerializer):
    class Meta:
        model = Transition
        fields = ['id', 'name', 'attribute_type']

class AllField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class FieldChoiceSerializer(serializers.Serializer):
    id = AllField(label='ID')
    name = serializers.CharField(label='名称')


class CustomFieldSerializer(CustomModelSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'


class CustomFieldCreateUpdateSerializer(CustomModelSerializer):

    field_choice = FieldChoiceSerializer(label='选项列表', many=True, required=False)

    class Meta:
        model = CustomField
        fields = ['workflow', 'field_type', 'field_key', 'field_name',
                  'sort', 'default_value', 'description', 'placeholder', 'field_template',
                  'boolean_field_display', 'field_choice', 'label', 'is_hidden']


class TicketSimpleSerializer(CustomModelSerializer):
    state_ = StateSimpleSerializer(source='state', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCreateSerializer(CustomModelSerializer):
    transition = serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all(), write_only=True)
    title = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Ticket
        fields = ['title', 'workflow', 'ticket_data', 'transition']

    def create(self, validated_data):
        return super().create(validated_data)


class TicketSerializer(CustomModelSerializer):
    workflow_ = WorkflowSimpleSerializer(source='workflow', read_only=True)
    state_ = StateSimpleSerializer(source='state', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('workflow', 'state')
        return queryset


class TicketListSerializer(CustomModelSerializer):
    workflow_ = WorkflowSimpleSerializer(source='workflow', read_only=True)
    state_ = StateSimpleSerializer(source='state', read_only=True)
    participant_ = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'sn', 'workflow', 'workflow_', 'state', 'state_',
                  'act_state', 'create_time', 'update_time', 'participant_type', 'create_by', 'ticket_data',
                  'participant_', 'script_run_last_result', 'participant']

    def get_participant_(self, obj):
        if obj.participant_type in [1, 2]:
            instance = User.objects.filter(id__in=obj.participant) | User.objects.filter(id=obj.participant)
            return UserSimpleSerializer(instance=instance, many=True).data
        return None

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('workflow', 'state')
        return queryset


class TicketDetailSerializer(CustomModelSerializer):
    workflow_ = WorkflowSimpleSerializer(source='workflow', read_only=True)
    state_ = StateSimpleSerializer(source='state', read_only=True)
    ticket_data_ = serializers.SerializerMethodField()
    participant_ = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'

    def get_participant_(self, obj):
        if obj.participant_type in [1, 2]:
            instance = User.objects.filter(id__in=obj.participant) | User.objects.filter(id=obj.participant)
            return UserSimpleSerializer(instance=instance, many=True).data
        return None

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('workflow', 'state')
        return queryset

    def get_ticket_data_(self, obj):
        ticket_data = obj.ticket_data
        state_fields = obj.state.state_fields
        all_fields = CustomField.objects.filter(workflow=obj.workflow).order_by('sort')
        all_fields_l = CustomFieldSerializer(instance=all_fields, many=True).data
        for i in all_fields_l:
            key = i['field_key']
            i['field_state'] = state_fields.get(key, 1)
            i['field_value'] = ticket_data.get(key, None)
            i['field_display'] = i['field_value']  # 该字段是用于查看详情直接展示
            if i['field_value']:
                if 'sys_user' in i['label']:
                    if isinstance(i['field_value'], list):
                        i['field_display'] = ','.join(list(User.objects.filter(
                            id__in=i['field_value']).values_list('name', flat=True)))
                    else:
                        f_obj = User.objects.filter(id=i['field_value']).first()
                        if f_obj:
                            i['field_display'] = f_obj.name
                elif 'deptSelect' in i['label']:
                    if isinstance(i['field_value'], list):
                        i['field_display'] = ','.join(list(Dept.objects.filter(
                            id__in=i['field_value']).values_list('name', flat=True)))
                    else:
                        f_obj = Dept.objects.filter(id=i['field_value']).first()
                        if f_obj:
                            i['field_display'] = f_obj.name
                elif i['field_type'] in ['radio', 'select']:
                    for m in i['field_choice']:
                        if m['id'] == i['field_value']:
                            i['field_display'] = m['name']
                elif i['field_type'] in ['checkbox', 'selects']:
                    d_list = []
                    for m in i['field_choice']:
                        if m['id'] in i['field_value']:
                            d_list.append(m['name'])
                    i['field_display'] = ','.join(d_list)
        return all_fields_l

    def filter_display(self, item, field_value):
        if item['id'] == field_value:
            return


class TicketFlowSerializer(CustomModelSerializer):
    participant_ = UserSignatureSerializer(source='participant', read_only=True)
    state_ = StateSimpleSerializer(source='state', read_only=True)
    transition_ = TransitionSimpleSerializer(source='transition', read_only=True)
    transition_attribute = serializers.CharField(source='transition.attribute_type', read_only=True)

    class Meta:
        model = TicketFlow
        fields = '__all__'


class TicketFlowSimpleSerializer(CustomModelSerializer):
    participant_ = UserSignatureSerializer(source='participant', read_only=True)
    state_ = StateSimpleSerializer(source='state', read_only=True)
    transition_ = TransitionSimpleSerializer(source='transition', read_only=True)
    transition_attribute = serializers.CharField(source='transition.attribute_type', read_only=True)

    class Meta:
        model = TicketFlow
        exclude = ['ticket_data']


class TicketHandleSerializer(serializers.Serializer):
    transition = serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all(), label="流转id")
    ticket_data = serializers.JSONField(label="表单数据json")
    suggestion = serializers.CharField(label="处理意见", required=False, allow_blank=True)


class TicketDeliverSerializer(serializers.Serializer):
    target_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), label='转交人')
    suggestion = serializers.CharField(label="转交原因", required=False)


class TicketRetreatSerializer(serializers.Serializer):
    suggestion = serializers.CharField(label="撤回原因", required=False)


class TicketCloseSerializer(serializers.Serializer):
    suggestion = serializers.CharField(label="关闭原因", required=False)


class TicketAddNodeSerializer(serializers.Serializer):
    suggestion = serializers.CharField(label="加签说明", required=False)
    toadd_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), label='发送给谁去加签')


class TicketAddNodeEndSerializer(serializers.Serializer):
    suggestion = serializers.CharField(label="加签意见", required=False)


class TicketDestorySerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all()), label='工单ID列表')


class TicketStateUpateSerializer(serializers.ModelSerializer):
    suggestion = serializers.CharField(label="变更理由", required=False)
    need_log = serializers.BooleanField(label="是否记录日志", default=True)

    class Meta:
        model = Ticket
        fields = ['state', 'suggestion', 'need_log']

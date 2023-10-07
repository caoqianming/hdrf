# Generated by Django 3.2.12 on 2022-08-15 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('key', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态标识')),
                ('is_hidden', models.BooleanField(default=False, help_text='设置为True时,获取工单步骤api中不显示此状态(当前处于此状态时除外)', verbose_name='是否隐藏')),
                ('sort', models.IntegerField(default=0, help_text='用于工单步骤接口时，step上状态的顺序(因为存在网状情况，所以需要人为设定顺序),值越小越靠前', verbose_name='状态顺序')),
                ('type', models.IntegerField(choices=[(0, '普通'), (1, '开始'), (2, '结束')], default=0, help_text='0.普通类型 1.初始状态(用于新建工单时,获取对应的字段必填及transition信息) 2.结束状态(此状态下的工单不得再处理，即没有对应的transition)', verbose_name='状态类型')),
                ('enable_retreat', models.BooleanField(default=False, help_text='开启后允许工单创建人在此状态直接撤回工单到初始状态', verbose_name='允许撤回')),
                ('enable_deliver', models.BooleanField(default=False, verbose_name='允许转交')),
                ('participant_type', models.IntegerField(blank=True, choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (10, '岗位'), (6, '脚本'), (7, '工单的字段'), (9, '代码获取')], default=1, help_text='0.无处理人,1.个人,2.多人,3.部门,4.角色,5.变量(支持工单创建人,创建人的leader),6.脚本,7.工单的字段内容(如表单中的"测试负责人"，需要为用户名或者逗号隔开的多个用户名),8.父工单的字段内容。 初始状态请选择类型5，参与人填create_by', verbose_name='参与者类型')),
                ('participant', models.JSONField(blank=True, default=list, help_text='可以为空(无处理人的情况，如结束状态)、userid、userid列表\\部门id\\角色id\\变量(create_by,create_by_tl)\\脚本记录的id等，包含子工作流的需要设置处理人为loonrobot', verbose_name='参与者')),
                ('state_fields', models.JSONField(blank=True, default=dict, help_text='json格式字典存储,包括读写属性1：只读，2：必填，3：可选, 4:隐藏 示例：{"create_time":1,"title":2, "sn":1}, 内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,workflow.workflow_name:工作流名称', verbose_name='表单字段')),
                ('distribute_type', models.IntegerField(choices=[(1, '主动接单'), (2, '直接处理'), (3, '随机分配'), (4, '全部处理')], default=1, help_text='1.主动接单(如果当前处理人实际为多人的时候，需要先接单才能处理) 2.直接处理(即使当前处理人实际为多人，也可以直接处理) 3.随机分配(如果实际为多人，则系统会随机分配给其中一个人) 4.全部处理(要求所有参与人都要处理一遍,才能进入下一步)', verbose_name='分配方式')),
                ('filter_dept', models.CharField(blank=True, max_length=20, null=True, verbose_name='部门字段过滤')),
                ('participant_cc', models.JSONField(blank=True, default=list, help_text='抄送给(userid列表)', verbose_name='抄送给')),
                ('on_reach_func', models.CharField(blank=True, max_length=100, null=True, verbose_name='到达时调用方法')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '工作流节点',
                'verbose_name_plural': '工作流节点',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('title', models.CharField(blank=True, help_text='工单标题', max_length=500, null=True, verbose_name='标题')),
                ('sn', models.CharField(help_text='工单的流水号', max_length=25, verbose_name='流水号')),
                ('ticket_data', models.JSONField(default=dict, help_text='工单自定义字段内容', verbose_name='工单数据')),
                ('in_add_node', models.BooleanField(default=False, help_text='是否处于加签状态下', verbose_name='加签状态中')),
                ('script_run_last_result', models.BooleanField(default=True, verbose_name='脚本最后一次执行结果')),
                ('participant_type', models.IntegerField(choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (10, '岗位'), (6, '脚本'), (7, '工单的字段'), (9, '代码获取')], default=0, help_text='0.无处理人,1.个人,2.多人', verbose_name='当前处理人类型')),
                ('participant', models.JSONField(blank=True, default=list, help_text='可以为空(无处理人的情况，如结束状态)、userid、userid列表', verbose_name='当前处理人')),
                ('act_state', models.IntegerField(choices=[(0, '草稿中'), (1, '进行中'), (2, '被退回'), (3, '被撤回'), (4, '已完成'), (5, '已关闭')], default=1, help_text='当前工单的进行状态', verbose_name='进行状态')),
                ('multi_all_person', models.JSONField(blank=True, default=dict, help_text='需要当前状态处理人全部处理时实际的处理结果，json格式', verbose_name='全部处理的结果')),
                ('add_node_man', models.ForeignKey(blank=True, help_text='加签操作的人，工单当前处理人处理完成后会回到该处理人，当处于加签状态下才有效', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='加签人')),
                ('belong_dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket_belong_dept', to='system.dept', verbose_name='所属部门')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wf.ticket', verbose_name='父工单')),
                ('parent_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_parent_state', to='wf.state', verbose_name='父工单状态')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_state', to='wf.state', verbose_name='当前状态')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('key', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='工作流标识')),
                ('sn_prefix', models.CharField(default='hb', max_length=50, verbose_name='流水号前缀')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('view_permission_check', models.BooleanField(default=True, help_text='开启后，只允许工单的关联人(创建人、曾经的处理人)有权限查看工单', verbose_name='查看权限校验')),
                ('limit_expression', models.JSONField(blank=True, default=dict, help_text='限制周期({"period":24} 24小时), 限制次数({"count":1}在限制周期内只允许提交1次), 限制级别({"level":1} 针对(1单个用户 2全局)限制周期限制次数,默认特定用户);允许特定人员提交({"allow_persons":"zhangsan,lisi"}只允许张三提交工单,{"allow_depts":"1,2"}只允许部门id为1和2的用户提交工单，{"allow_roles":"1,2"}只允许角色id为1和2的用户提交工单)', verbose_name='限制表达式')),
                ('display_form_str', models.JSONField(blank=True, default=list, help_text='默认"[]"，用于用户只有对应工单查看权限时显示哪些字段,field_key的list的json,如["days","sn"],内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,workflow.workflow_name:工作流名称', verbose_name='展现表单字段')),
                ('title_template', models.CharField(blank=True, default='{title}', help_text='工单字段的值可以作为参数写到模板中，格式如：你有一个待办工单:{title}', max_length=50, null=True, verbose_name='标题模板')),
                ('content_template', models.CharField(blank=True, default='标题:{title}, 创建时间:{create_time}', help_text='工单字段的值可以作为参数写到模板中，格式如：标题:{title}, 创建时间:{create_time}', max_length=1000, null=True, verbose_name='内容模板')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='操作')),
                ('timer', models.IntegerField(default=0, help_text='单位秒。处于源状态X秒后如果状态都没有过变化则自动流转到目标状态。设置时间有效', verbose_name='定时器(单位秒)')),
                ('condition_expression', models.JSONField(blank=True, default=list, help_text='流转条件表达式，根据表达式中的条件来确定流转的下个状态，格式为[{"expression":"{days} > 3 and {days}<10", "target_state":11}] 其中{}用于填充工单的字段key,运算时会换算成实际的值，当符合条件下个状态将变为target_state_id中的值,表达式只支持简单的运算或datetime/time运算.loonflow会以首次匹配成功的条件为准，所以多个条件不要有冲突', verbose_name='条件表达式')),
                ('attribute_type', models.IntegerField(choices=[(1, '同意'), (2, '拒绝'), (3, '其他')], default=1, help_text='属性类型，1.同意，2.拒绝，3.其他', verbose_name='属性类型')),
                ('field_require_check', models.BooleanField(default=True, help_text='默认在用户点击操作的时候需要校验工单表单的必填项,如果设置为否则不检查。用于如"退回"属性的操作，不需要填写表单内容', verbose_name='是否校验必填项')),
                ('on_submit_func', models.CharField(blank=True, max_length=100, null=True, verbose_name='提交操作调用方法')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transition_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('destination_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dstate_transition', to='wf.state', verbose_name='目的状态')),
                ('source_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sstate_transition', to='wf.state', verbose_name='源状态')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transition_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wf.workflow', verbose_name='所属工作流')),
            ],
            options={
                'verbose_name': '工作流流转',
                'verbose_name_plural': '工作流流转',
            },
        ),
        migrations.CreateModel(
            name='TicketFlow',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('suggestion', models.CharField(blank=True, default='', max_length=10000, verbose_name='处理意见')),
                ('participant_type', models.IntegerField(choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (10, '岗位'), (6, '脚本'), (7, '工单的字段'), (9, '代码获取')], default=0, help_text='0.无处理人,1.个人,2.多人等', verbose_name='处理人类型')),
                ('participant_str', models.CharField(blank=True, help_text='非人工处理的处理人相关信息', max_length=200, null=True, verbose_name='处理人')),
                ('ticket_data', models.JSONField(blank=True, default=dict, help_text='可以用于记录当前表单数据，json格式', verbose_name='工单数据')),
                ('intervene_type', models.IntegerField(choices=[(0, '正常处理'), (1, '转交'), (2, '加签'), (3, '加签处理完成'), (4, '接单'), (5, '评论'), (6, '删除'), (7, '强制关闭'), (8, '强制修改状态'), (9, 'hook操作'), (10, '撤回'), (11, '抄送')], default=0, help_text='流转类型', verbose_name='干预类型')),
                ('participant_cc', models.JSONField(blank=True, default=list, help_text='抄送给(userid列表)', verbose_name='抄送给')),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticketflow_participant', to=settings.AUTH_USER_MODEL, verbose_name='处理人')),
                ('state', models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='wf.state', verbose_name='当前状态')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketflow_ticket', to='wf.ticket', verbose_name='关联工单')),
                ('transition', models.ForeignKey(blank=True, help_text='与worklow.Transition关联, 为空时表示认为干预的操作', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wf.transition', verbose_name='流转id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wf.workflow', verbose_name='关联工作流'),
        ),
        migrations.AddField(
            model_name='state',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wf.workflow', verbose_name='所属工作流'),
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('field_type', models.CharField(choices=[('string', '字符串'), ('int', '整型'), ('float', '浮点'), ('boolean', '布尔'), ('date', '日期'), ('datetime', '日期时间'), ('radio', '单选'), ('checkbox', '多选'), ('select', '单选下拉'), ('selects', '多选下拉'), ('cascader', '单选级联'), ('cascaders', '多选级联'), ('select_dg', '弹框单选'), ('select_dgs', '弹框多选'), ('textarea', '文本域'), ('file', '附件'), ('table', '表格')], help_text='string, int, float, date, datetime, radio, checkbox, select, selects, cascader, cascaders, select_dg, select_dgs,textarea, file', max_length=50, verbose_name='类型')),
                ('field_key', models.CharField(help_text='字段类型请尽量特殊，避免与系统中关键字冲突', max_length=50, verbose_name='字段标识')),
                ('field_name', models.CharField(max_length=50, verbose_name='字段名称')),
                ('sort', models.IntegerField(default=0, help_text='工单基础字段在表单中排序为:流水号0,标题20,状态id40,状态名41,创建人80,创建时间100,更新时间120.前端展示工单信息的表单可以根据这个id顺序排列', verbose_name='排序')),
                ('default_value', models.CharField(blank=True, help_text='前端展示时，可以将此内容作为表单中的该字段的默认值', max_length=100, null=True, verbose_name='默认值')),
                ('description', models.CharField(blank=True, help_text='字段的描述信息，可用于显示在字段的下方对该字段的详细描述', max_length=100, null=True, verbose_name='描述')),
                ('placeholder', models.CharField(blank=True, help_text='用户工单详情表单中作为字段的占位符显示', max_length=100, null=True, verbose_name='占位符')),
                ('field_template', models.TextField(blank=True, help_text='文本域类型字段前端显示时可以将此内容作为字段的placeholder', null=True, verbose_name='文本域模板')),
                ('boolean_field_display', models.JSONField(blank=True, default=dict, help_text='当为布尔类型时候，可以支持自定义显示形式。{"1":"是","0":"否"}或{"1":"需要","0":"不需要"}，注意数字也需要引号', verbose_name='布尔类型显示名')),
                ('field_choice', models.JSONField(blank=True, default=list, help_text='选项值，格式为list, 例["id":1, "name":"张三"]', verbose_name='选项值')),
                ('label', models.CharField(default='', help_text='处理特殊逻辑使用,比如sys_user用于获取用户作为选项', max_length=1000, verbose_name='标签')),
                ('is_hidden', models.BooleanField(default=False, help_text='可用于携带不需要用户查看的字段信息', verbose_name='是否隐藏')),
                ('group', models.CharField(blank=True, max_length=100, null=True, verbose_name='字段分组')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customfield_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wf.customfield', verbose_name='父字段')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customfield_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wf.workflow', verbose_name='所属工作流')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

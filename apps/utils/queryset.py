from django.apps import apps
from django.db.models import Q


def get_child_queryset_u(checkQueryset, hasParent=True):
    '''
    获取所有子集
    查的范围checkQueryset
    父obj
    是否包含父默认True
    若有parent_link字段则进行性能优化
    '''
    cls = type(checkQueryset.model)
    if hasattr(cls, 'parent'):
        queryset = cls.objects.none()
        if hasattr(cls, 'parent_link'):
            for item in checkQueryset:
                queryset = queryset | cls.objects.filter(parent_link__contains=item.id)
                if hasParent:
                    queryset = queryset | cls.objects.filter(pk=item.id)
            return queryset
        if hasParent:
            queryset = checkQueryset
        child_queryset = checkQueryset.filter(parent__in=queryset)
        while child_queryset.exists():
            queryset = queryset | child_queryset
            child_queryset = checkQueryset.filter(parent__in=child_queryset)
        return queryset
    elif hasParent:
        return checkQueryset
    else:
        return checkQueryset.none()


def get_child_queryset(name, pk, hasParent=True):
    '''
    获取所有子集
    app.model名称
    Id
    是否包含父默认True
    '''
    app, model = name.split('.')
    cls = apps.get_model(app, model)
    queryset = cls.objects.none()
    fatherQueryset = cls.objects.filter(pk=pk)
    if fatherQueryset.exists():
        if hasParent:
            queryset = fatherQueryset
        child_queryset = cls.objects.filter(parent=fatherQueryset.first())
        while child_queryset.exists():
            queryset = queryset | child_queryset
            child_queryset = cls.objects.filter(parent__in=child_queryset)
    return queryset


def get_child_queryset2(obj, hasParent=True):
    '''
    获取所有子集
    obj实例
    数据表需包含parent字段
    是否包含父默认True
    '''
    cls = type(obj)
    queryset = cls.objects.none()
    if hasParent:
        queryset = cls.objects.filter(pk=obj.id)
    child_queryset = cls.objects.filter(parent=obj)
    while child_queryset.exists():
        queryset = queryset | child_queryset
        child_queryset = cls.objects.filter(parent__in=child_queryset)
    return queryset


def get_parent_queryset(obj, hasSelf=True):
    cls = type(obj)
    ids = []
    if hasSelf:
        ids.append(obj.id)
    while obj.parent:
        obj = obj.parent
        ids.append(obj.id)
    return cls.objects.filter(id__in=ids)

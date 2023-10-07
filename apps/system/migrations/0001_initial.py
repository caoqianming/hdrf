# Generated by Django 3.2.12 on 2022-08-15 06:02

import apps.system.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('type', models.CharField(default='employee', max_length=10, verbose_name='账号类型')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='姓名')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('avatar', models.CharField(blank=True, default='/media/default/avatar.png', max_length=100, null=True, verbose_name='头像')),
                ('secret', models.CharField(blank=True, max_length=100, null=True, verbose_name='密钥')),
                ('wx_openid', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信公众号OpenId')),
                ('wx_nickname', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信昵称')),
                ('wx_headimg', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信头像')),
                ('wxmp_openid', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信小程序OpenId')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['create_time'],
            },
            managers=[
                ('objects', apps.system.models.SoftDeletableUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('type', models.CharField(default='dept', max_length=20, verbose_name='类型')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序标记')),
                ('third_info', models.JSONField(default=dict, verbose_name='三方系统信息')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dept_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dept', verbose_name='父')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dept_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('type', models.PositiveSmallIntegerField(choices=[(10, '目录'), (20, '菜单'), (30, '按钮')], default=30, verbose_name='类型')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序标记')),
                ('codes', models.JSONField(blank=True, default=list, null=True, verbose_name='权限标识')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.permission', verbose_name='父')),
            ],
            options={
                'verbose_name': '功能权限表',
                'verbose_name_plural': '功能权限表',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='岗位标识')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('min_hour', models.PositiveSmallIntegerField(default=0, verbose_name='最小在岗时间')),
                ('max_hour', models.PositiveSmallIntegerField(default=12, verbose_name='最长在岗时间')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.post', verbose_name='父')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '职位/岗位',
                'verbose_name_plural': '职位/岗位',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='名称')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='up_dept', to='system.dept')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='up_post', to='system.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='up_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户岗位关系表',
                'verbose_name_plural': '用户岗位关系表',
                'ordering': ['sort', 'create_time'],
                'unique_together': {('user', 'post', 'dept')},
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='角色标识')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('perms', models.ManyToManyField(blank=True, related_name='role_perms', to='system.Permission', verbose_name='功能权限')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='PostRole',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('data_range', models.PositiveSmallIntegerField(choices=[(10, '全部'), (30, '同级及以下'), (40, '本级及以下'), (50, '本级'), (60, '仅本人')], default=40, verbose_name='数据权限范围')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.post', verbose_name='关联岗位')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.role', verbose_name='关联角色')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名称')),
                ('size', models.IntegerField(blank=True, default=1, null=True, verbose_name='文件大小')),
                ('file', models.FileField(upload_to='%Y/%m/%d/', verbose_name='文件')),
                ('mime', models.CharField(blank=True, max_length=120, null=True, verbose_name='文件格式')),
                ('type', models.CharField(choices=[(10, '文档'), (20, '视频'), (30, '音频'), (40, '图片'), (50, '其它')], default='文档', max_length=50, verbose_name='文件类型')),
                ('path', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '文件库',
                'verbose_name_plural': '文件库',
            },
        ),
        migrations.CreateModel(
            name='DictType',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('code', models.CharField(max_length=30, verbose_name='标识')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicttype_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dicttype', verbose_name='父')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicttype_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '字典类型',
                'verbose_name_plural': '字典类型',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='belong_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_belong_dept', to='system.dept', verbose_name='所属部门'),
        ),
        migrations.AddField(
            model_name='user',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='user',
            name='depts',
            field=models.ManyToManyField(through='system.UserPost', to='system.Dept'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.post', verbose_name='主要岗位'),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ManyToManyField(related_name='user_posts', through='system.UserPost', to='system.Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='system.Role', verbose_name='关联角色'),
        ),
        migrations.AddField(
            model_name='user',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='上级主管'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.CharField(editable=False, help_text='主键ID', max_length=20, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('value', models.CharField(blank=True, max_length=10, null=True, verbose_name='值')),
                ('code', models.CharField(blank=True, max_length=30, null=True, verbose_name='标识')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('is_used', models.BooleanField(default=True, verbose_name='是否有效')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dictionary_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dictionary', verbose_name='父')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.dicttype', verbose_name='类型')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dictionary_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人')),
            ],
            options={
                'verbose_name': '字典',
                'verbose_name_plural': '字典',
                'ordering': ['sort'],
                'unique_together': {('name', 'is_used', 'type')},
            },
        ),
    ]

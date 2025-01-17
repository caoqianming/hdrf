# Generated by Django 3.2.12 on 2024-06-05 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_permission_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent',
        ),
        migrations.AddField(
            model_name='dept',
            name='parent_link',
            field=models.JSONField(blank=True, default=list, editable=False, verbose_name='父级关联'),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='parent_link',
            field=models.JSONField(blank=True, default=list, editable=False, verbose_name='父级关联'),
        ),
        migrations.AddField(
            model_name='dicttype',
            name='parent_link',
            field=models.JSONField(blank=True, default=list, editable=False, verbose_name='父级关联'),
        ),
        migrations.AddField(
            model_name='permission',
            name='parent_link',
            field=models.JSONField(blank=True, default=list, editable=False, verbose_name='父级关联'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='parent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dept', verbose_name='父'),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='parent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dictionary', verbose_name='父'),
        ),
        migrations.AlterField(
            model_name='dicttype',
            name='parent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.dicttype', verbose_name='父'),
        ),
    ]

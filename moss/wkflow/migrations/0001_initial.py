# Generated by Django 2.2.4 on 2019-08-11 11:44

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default='new', help_text='工单状态', max_length=50, verbose_name='状态')),
                ('sn', models.CharField(help_text='工单的流水号', max_length=12, unique=True, verbose_name='流水号')),
                ('title', models.CharField(default='', help_text='工单的标题', max_length=50, verbose_name='标题')),
                ('content', models.TextField(default='', help_text='工单内容描述', max_length=200, verbose_name='工单内容')),
                ('level', models.CharField(choices=[(1, 'P1'), (2, 'P2'), (3, 'P3'), (4, 'P4'), (5, 'P5')], default=2, max_length=3, verbose_name='工单等级')),
                ('creator', models.CharField(help_text='工单创建人', max_length=12, verbose_name='创建者')),
                ('contact_man', models.CharField(help_text='告障或委托人姓名', max_length=12, verbose_name='告障人')),
                ('contact_number', models.CharField(help_text='告障或委托人手机号码', max_length=11, verbose_name='联系电话')),
                ('contact_org', models.CharField(help_text='告障或委托单位', max_length=50, verbose_name='告障单位')),
                ('gmt_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('assigner', models.CharField(default='ROBOT', help_text='工单分派与调度', max_length=12, verbose_name='调度人')),
                ('gmt_assigned', models.DateTimeField(null=True, verbose_name='指派时间')),
                ('executor', models.CharField(blank=True, default='', help_text='工单处理人', max_length=12, verbose_name='处理人')),
                ('gmt_accepted', models.DateTimeField(null=True, verbose_name='接受时间')),
                ('is_closed', models.BooleanField(default=False, help_text='工单是否已关闭', verbose_name='已关闭')),
            ],
            options={
                'verbose_name': '工单记录',
                'verbose_name_plural': '工单记录',
            },
        ),
        migrations.CreateModel(
            name='TicketReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(blank=True, default='', help_text='工单处理完成后的复核与评价人', max_length=12, verbose_name='复核人')),
                ('comments', models.TextField(blank=True, default='', help_text='工单复核与评论', max_length=50, verbose_name='评论')),
                ('gmt_edit', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('sn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wkflow.TicketRecord', verbose_name='工单编号')),
            ],
        ),
        migrations.CreateModel(
            name='TicketHandle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.TextField(help_text='故障或需求描述', max_length=50, verbose_name='需求描述')),
                ('reason', models.TextField(help_text='故障或需求原因', max_length=50, verbose_name='原因分析')),
                ('process', models.TextField(help_text='处理过程', max_length=200, verbose_name='处理过程')),
                ('advices', models.TextField(help_text='技术优化建议', max_length=200, verbose_name='技术建议')),
                ('gmt_start', models.DateTimeField(verbose_name='开始处理时间')),
                ('gmt_done', models.DateTimeField(verbose_name='处理完成时间')),
                ('gmt_edit', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('sn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wkflow.TicketRecord', verbose_name='工单编号')),
            ],
            options={
                'verbose_name': '工单详情',
                'verbose_name_plural': '工单详情',
            },
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-11 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='部门')),
                ('desc', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'verbose_name': '组',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='角色')),
                ('desc', models.CharField(blank=True, max_length=64, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=32, unique=True)),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
                ('avatar', models.TextField(blank=True, null=True, verbose_name='头像')),
                ('create_date', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, to='users.Group', verbose_name='部门')),
                ('roles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Role', verbose_name='角色')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]

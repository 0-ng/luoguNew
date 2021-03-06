# Generated by Django 2.2.6 on 2020-06-16 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('no', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('title', models.CharField(default='', max_length=50)),
                ('question', models.CharField(default='', max_length=500)),
                ('answer', models.CharField(default='', max_length=500)),
                ('tag', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('difficulty', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('accepted', models.IntegerField(blank=True, default=0, null=True)),
                ('attempted', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=5)),
                ('no', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motto', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('region', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'myUser',
            },
        ),
    ]

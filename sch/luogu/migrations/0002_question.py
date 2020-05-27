# Generated by Django 2.2.6 on 2020-05-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luogu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=20, null=True)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('accepted', models.IntegerField()),
                ('attempted', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2020-06-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luogu', '0003_auto_20200616_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Contributions',
            },
        ),
    ]

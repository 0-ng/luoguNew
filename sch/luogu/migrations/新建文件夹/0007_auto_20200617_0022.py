# Generated by Django 2.2.6 on 2020-06-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luogu', '0006_auto_20200616_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]

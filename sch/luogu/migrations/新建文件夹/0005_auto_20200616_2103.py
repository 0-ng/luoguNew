# Generated by Django 2.2.6 on 2020-06-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luogu', '0004_contributions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='luogu.Tag'),
        ),
    ]

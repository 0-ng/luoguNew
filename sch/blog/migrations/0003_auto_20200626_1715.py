# Generated by Django 2.2.6 on 2020-06-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200621_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img/%Y/%m/%d/', verbose_name='文章图片'),
        ),
    ]

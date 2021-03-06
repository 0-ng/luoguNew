# Generated by Django 2.2.6 on 2020-06-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luogu', '0005_auto_20200616_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, choices=[(1, '函数与极限'), (2, '导数与微分'), (3, '微分中值定理与导数的应用'), (4, '不定积分'), (5, '定积分'), (6, '微分方程'), (7, '向量代数与空间解析几何'), (8, '多元函数微分法及其应用'), (9, '重积分'), (10, '曲线积分与曲面积分'), (11, '无穷级数')], default='', max_length=100, null=True),
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class myUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    motto = models.CharField(max_length=100, null=True, blank=True, default="")
    # pic = models.CharField(max_length=50, null=True, blank=True, default="")
    region = models.CharField(max_length=60, null=True, blank=True, default="")

    def __str__(self):
        return self.user.username
    class Meta:
        db_table="myUser"


class Tag(models.Model):
    # choices = (
    #     (1, '函数与极限'),
    #     (2, '导数与微分'),
    #     (3, '微分中值定理与导数的应用'),
    #     (4, '不定积分'),
    #     (5, '定积分'),
    #     (6, '微分方程'),
    #     (7, '向量代数与空间解析几何'),
    #     (8, '多元函数微分法及其应用'),
    #     (9, '重积分'),
    #     (10, '曲线积分与曲面积分'),
    #     (11, '无穷级数'),
    # )
    # name = models.CharField(max_length=100, null=True, blank=True, default="", choices=choices)
    name = models.CharField(max_length=100, null=True, blank=True, default="", unique=True)
    def __str__(self):
        return self.name


class Question(models.Model):
    subject = models.CharField(max_length=5, null=True, blank=True, default="")
    no = models.CharField(max_length=6, null=True, blank=True, default="")
    title = models.CharField(max_length=50, null=False, blank=False, default="")
    question = models.CharField(max_length=500, null=False, blank=False, default="")
    answer = models.CharField(max_length=500, null=False, blank=False, default="")
    tag = models.ManyToManyField(Tag)
    difficulty = models.CharField(max_length=20, null=True, blank=True, default="")
    accepted = models.IntegerField(null=True, blank=True, default=0)
    attempted = models.IntegerField(null=True, blank=True, default=0)
    pass_ratio = models.FloatField(null=True, blank=True, default=0)
    status = models.IntegerField(null=False, blank=False, default=0)
    score = models.IntegerField(null=False, blank=False, default=0)
    def __str__(self):
        return self.no

    class Meta:
        db_table="Question"


class Status(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, default="")
    subject = models.CharField(max_length=5, null=False, blank=False, default="")
    no = models.CharField(max_length=6, null=True, blank=True, default="")
    status = models.IntegerField(null=False, blank=False, default=0)
    def __str__(self):
        return self.username + " " + self.no
    class Meta:
        db_table="Status"


class Contributions(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, default="")
    date = models.DateField(auto_now_add=True)
    num = models.IntegerField(null=False, blank=False, default=0)
    class Meta:
        db_table="Contributions"


class History(models.Model):
    '''做题历史'''
    username = models.CharField(max_length=50, null=False, blank=False, default="")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(null=False, blank=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="History"
        get_latest_by = "date"
    def __str__(self):
        return self.username + " " + self.question.no


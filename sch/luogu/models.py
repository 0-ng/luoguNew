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


class Question(models.Model):
    subject = models.CharField(max_length=5, null=True, blank=True, default="")
    # no = models.IntegerField(null=False, blank=False)
    no = models.CharField(max_length=6, null=True, blank=True, default="")
    title = models.CharField(max_length=50, null=False, blank=False, default="")
    question = models.CharField(max_length=500, null=False, blank=False, default="")
    answer = models.CharField(max_length=500, null=False, blank=False, default="")
    tag = models.CharField(max_length=20, null=True, blank=True, default="")
    difficulty = models.CharField(max_length=20, null=True, blank=True, default="")
    accepted = models.IntegerField(null=True, blank=True, default=0)
    attempted = models.IntegerField(null=True, blank=True, default=0)
    status = models.IntegerField(null=False, blank=False, default=0)
    def __str__(self):
        return self.no


    class Meta:
        db_table="Question"


class Status(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, default="")
    subject = models.CharField(max_length=5, null=False, blank=False, default="")
    # no = models.IntegerField(null=False, blank=False)
    no = models.CharField(max_length=6, null=True, blank=True, default="")
    status = models.IntegerField(null=False, blank=False, default=0)
    def __str__(self):
        return self.no
    class Meta:
        db_table="Status"


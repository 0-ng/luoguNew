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


class Question(models.Model):
    subject = models.CharField(max_length=5, null=True, blank=True)
    no = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    question = models.CharField(max_length=500, null=False, blank=False)
    answer = models.CharField(max_length=500, null=False, blank=False)
    tag = models.CharField(max_length=20, null=True, blank=True)
    difficulty = models.CharField(max_length=20, null=True, blank=True)
    accepted = models.IntegerField(null=True, blank=True)
    attempted = models.IntegerField(null=True, blank=True)


class Status(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=5, null=False, blank=False)
    no = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)


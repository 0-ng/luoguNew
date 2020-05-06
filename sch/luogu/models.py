from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LuoguUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    motto = models.CharField(max_length=100, null=True, blank=True, default="")
    pic = models.CharField(max_length=50, null=True, blank=True, default="")
    region = models.CharField(max_length=60, null=True, blank=True, default="")

    def __str__(self):
        return self.user.username


# class Status(models.Model):
#     user = models.ForeignKey(WeChatUser, models.CASCADE)
#     text = models.CharField(max_length=280)
#     pics = models.CharField(max_length=100, null=True, blank=True)
#     pub_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text
#
#     class Meta:
#         ordering = ["-id"]
#
#
# class Reply(models.Model):
#     status = models.ForeignKey(Status, models.CASCADE)
#     author = models.CharField(max_length=50)
#     type = models.CharField(max_length=10, choices=(("0", "like"), ("1", "comment")))
#     at_person = models.CharField(max_length=50, null=True, blank=True)
#     text = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return "{} on {}".format(self.author, self.status)



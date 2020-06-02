from django.contrib import admin
from .models import myUser, Question
# Register your models here.
admin.site.register(myUser)
admin.site.register(Question)
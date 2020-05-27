from django.contrib import admin
from .models import LuoguUser, Question
# Register your models here.
admin.site.register(LuoguUser)
admin.site.register(Question)
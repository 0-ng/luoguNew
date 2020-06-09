from django.contrib import admin
from .models import myUser, Question, Status
# Register your models here.
admin.site.register(myUser)
admin.site.register(Question)
admin.site.register(Status)
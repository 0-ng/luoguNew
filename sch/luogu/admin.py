from django.contrib import admin
from .models import myUser, Question, Status, Tag, History, Note
# Register your models here.
admin.site.register(myUser)
admin.site.register(Question)
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(History)
admin.site.register(Note)
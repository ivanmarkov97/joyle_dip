from django.contrib import admin
from .models import Group, Chat, Message
# Register your models here.

admin.site.register(Group)
admin.site.register(Chat)
admin.site.register(Message)

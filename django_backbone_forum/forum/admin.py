from django.contrib import admin
from .models import Thread, Message


class ThreadAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message, MessageAdmin)

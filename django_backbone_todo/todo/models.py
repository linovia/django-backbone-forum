from django.db import models


class Thread(models.Model):
    title = models.CharField(max_length=64)


class Message(models.Model):
    thread = models.ForeignKey(Thread, related_name='messages')
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128)
    text = models.TextField()

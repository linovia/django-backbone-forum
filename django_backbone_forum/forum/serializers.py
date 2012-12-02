from .models import Thread, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source='id', read_only=True)
    date_added = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = ('_id', 'author', 'text', 'thread')


class ThreadSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source='id', read_only=True)
    messages = MessageSerializer(source='messages')

    class Meta:
        model = Thread
        fields = ('_id', 'title', 'messages')

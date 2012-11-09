from .models import Thread, Message
from rest_framework import serializers


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        # fields = ('title', )
        fields = ('id', 'title', )
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    # thread = ThreadSerializer()
    date_added = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'date_added', 'author', 'text', 'thread')

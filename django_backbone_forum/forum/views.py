from .models import Thread, Message
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import ThreadSerializer, MessageSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'threads': reverse('thread-list', request=request),
        'messages': reverse('message-list', request=request),
    })


class ThreadList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of threads.
    """
    model = Thread
    serializer_class = ThreadSerializer


class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single thread.
    """
    model = Thread
    serializer_class = ThreadSerializer


class MessageList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of messages.
    """
    model = Message
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single message.
    """
    model = Message
    serializer_class = MessageSerializer

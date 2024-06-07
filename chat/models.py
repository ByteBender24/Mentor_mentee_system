from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    # Add necessary fields for the chat room, e.g., mentor, mentee, timestamp, etc.
    class Meta:
        app_label = 'chat'


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

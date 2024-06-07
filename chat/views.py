# chat/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import ChatRoom, Message

def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, pk=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

def send_message(request):
    room_id = request.POST.get('room_id')
    content = request.POST.get('content')
    # Save the message to the database
    room = get_object_or_404(ChatRoom, pk=room_id)
    message = Message(room=room, sender=request.user, content=content)
    message.save()
    # Broadcast the message to all connected clients in the room
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"chat_{room_id}",
        {
            'type': 'chat_message',
            'message': {
                'sender': message.sender.username,
                'content': message.content,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }
        }
    )
    return JsonResponse({'status': 'ok'})




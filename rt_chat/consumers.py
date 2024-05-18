from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
import json
from .models import *


class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        # self.user = self.scope['user']
        # self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        # self.chatroom = get_object_or_404(chatGrp,group_name=self.chatroom_name)
        self.accept() 

    # def receive(self,text_data):
    #     text_data_json = json.loads(text_data)
    #     body = text_data_json['body']

    #     message = grpMsg.objects.create(
    #         body = body,
    #         author = self.user,
    #         group = self.chatroom
    #     )
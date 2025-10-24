import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    # Signals ke through ye call hoga
    async def send_notification(self, event):
        title = event['title']
        await self.send(text_data=json.dumps({
            "title": title
        }))

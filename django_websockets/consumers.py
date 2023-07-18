"""
Websocket consumers
"""

from channels.generic.websocket import AsyncWebsocketConsumer


class SimpleConsumer(AsyncWebsocketConsumer):
    """Simple websocket consumer"""

    async def connect(self):
        """socket connection"""
        print('connected')
        await self.accept()

    async def disconnect(self, close_code):
        """socket disconnection"""
        print('disconnected', close_code)

    async def receive(self, text_data):
        """socket message"""
        print('received', text_data)
        await self.send(text_data=text_data)

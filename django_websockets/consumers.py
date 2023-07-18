"""
Websocket consumers
"""

import logging

from channels.generic.websocket import AsyncWebsocketConsumer


class SimpleConsumer(AsyncWebsocketConsumer):
    """Simple websocket consumer"""

    async def connect(self):
        """socket connection"""
        logging.debug('connected')
        await self.accept()
        await self.channel_layer.group_add('simple', self.channel_name)

    async def disconnect(self, close_code):
        """socket disconnection"""
        logging.debug('disconnected: %s', close_code)
        await self.channel_layer.group_discard('simple', self.channel_name)

    async def receive(self, text_data):
        """socket message"""
        logging.debug('received: %s', text_data)
        await self.channel_layer.group_send(
            'simple',
            {
                'type': 'simple.message',
                'message': text_data,
            }
        )

    async def simple_message(self, event):
        """socket group message"""
        logging.debug('group message: %s', event)
        await self.send(text_data=event['message'])

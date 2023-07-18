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

    async def disconnect(self, close_code):
        """socket disconnection"""
        logging.debug('disconnected: %s', close_code)

    async def receive(self, text_data):
        """socket message"""
        logging.debug('received: %s', text_data)
        await self.send(text_data=text_data)

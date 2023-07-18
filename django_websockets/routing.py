from django.urls import path
from django_websockets.consumers import SimpleConsumer

websocket_urlpatterns = [
    path('ws/', SimpleConsumer.as_asgi()),
]

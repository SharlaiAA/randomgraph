from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            num = randint(1, 100)
            await self.send(json.dumps({'value' : num}))
            await sleep(1.0)
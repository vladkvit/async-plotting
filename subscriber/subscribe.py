import aiozmq
import zmq
from typing import Callable

async def subscribe_to_messages(data_callback: Callable[[bytes], None] = None):
    subscriber = await aiozmq.create_zmq_stream(zmq.SUB, connect='tcp://localhost:5556')
    subscriber.transport.subscribe(b'topic')
    while True:
        topic, message = await subscriber.read()
        if data_callback:
            data_callback(message)
        print(f'Received: {message.decode("utf-8")}')
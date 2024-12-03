import aiozmq
import zmq
from typing import Callable


async def subscribe_to_messages(
    message_queue,
    data_callback: Callable[[bytes], None] = None,
):
    while True:
        message = await message_queue.get()
        if data_callback:
            data_callback(message)
        print(f'Received: {message.decode("utf-8")}')

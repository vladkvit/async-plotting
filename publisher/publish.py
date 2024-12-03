import random

import asyncio


async def publish_messages(message_queue):
    counter = 0
    while counter < 100:
        random_number = random.randint(0, 100)
        message = f"{random_number}".encode("utf-8")
        await message_queue.put(message)
        print(f"Published: {message}")
        await asyncio.sleep(1)
        counter += 1

import zmq
import aiozmq
import asyncio

async def publish_messages():
    publisher = await aiozmq.create_zmq_stream(zmq.PUB, bind='tcp://*:5556')

    counter = 0
    while counter < 100:
        message = f'{counter}'.encode('utf-8')
        publisher.write([b'topic', message])
        print(f'Published: {message}')
        await asyncio.sleep(1)
        counter += 1
    publisher.close()

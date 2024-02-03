import aiozmq
import zmq

async def subscribe_to_messages():
    subscriber = await aiozmq.create_zmq_stream(zmq.SUB, connect='tcp://localhost:5556')
    subscriber.transport.subscribe(b'topic')
    while True:
        topic, message = await subscriber.read()
        print(f'Received: {message.decode("utf-8")}')
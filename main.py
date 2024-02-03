import asyncio
from publisher.publish import publish_messages
from subscriber.subscribe import subscribe_to_messages

async def main():
    publisher_task = asyncio.create_task(publish_messages())
    subscriber_task = asyncio.create_task(subscribe_to_messages())

    await asyncio.gather(publisher_task, subscriber_task)

if __name__ == '__main__':
    asyncio.run(main())
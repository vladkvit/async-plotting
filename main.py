import asyncio
import threading
from publisher.publish import publish_messages
from subscriber.subscribe import subscribe_to_messages
from plotter.chart_plotter import plotter, update_data

message_queue = asyncio.Queue()


async def main():
    publisher_task = asyncio.create_task(publish_messages(message_queue))
    subscriber_task = asyncio.create_task(
        subscribe_to_messages(message_queue, update_data)
    )

    await asyncio.gather(publisher_task, subscriber_task)


def run_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())


if __name__ == "__main__":
    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=run_event_loop, args=(new_loop,))
    t.start()
    plotter()
    t.join()

import asyncio
import threading
from publisher.publish import publish_messages
from subscriber.subscribe import subscribe_to_messages
from plotter.chart_plotter import plotter, update_data

async def main():
    publisher_task = asyncio.create_task(publish_messages())
    subscriber_task = asyncio.create_task(subscribe_to_messages(update_data))

    await asyncio.gather(publisher_task, subscriber_task)

if __name__ == '__main__':
    plotting_thread = threading.Thread(target=plotter, daemon=True)
    plotting_thread.start()
    asyncio.run(main())
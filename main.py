import asyncio
import threading
import signal
from publisher.publish import publish_messages
from subscriber.subscribe import subscribe_to_messages
from plotter.chart_plotter import plotter, update_data

message_queue = asyncio.Queue()
shutdown_event = threading.Event()


async def main():
    publisher_task = asyncio.create_task(
        publish_messages(message_queue, shutdown_event)
    )
    subscriber_task = asyncio.create_task(
        subscribe_to_messages(message_queue, shutdown_event, update_data)
    )

    await asyncio.gather(publisher_task, subscriber_task, return_exceptions=True)


def run_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())


def signal_handler(signum, frame):
    print("Signal received, shutting down...")
    shutdown_event.set()  # Set the shutdown event


if __name__ == "__main__":
    # Register signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=run_event_loop, args=(new_loop,))
    t.start()
    plotter(shutdown_event)
    t.join()

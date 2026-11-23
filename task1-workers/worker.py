"""Run the job workers of process_order and process_payment until Ctrl+C."""

import asyncio
import logging

from pyzeebe import ZeebeClient, ZeebeWorker

import handlers
from connection import create_channel


async def main() -> None:
    channel = create_channel()
    handlers.set_client(ZeebeClient(channel))
    worker = ZeebeWorker(channel, name="desp-task1-workers")
    worker.include_router(handlers.router)
    types = sorted(task.type for task in handlers.router.tasks)
    logging.info("Waiting for jobs of %d types: %s", len(types), ", ".join(types))
    await worker.work()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    logging.getLogger("pyzeebe").setLevel(logging.WARNING)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Stopped")

import logging
import asyncio
import aiozmq
import zmq

logging.basicConfig(level=logging.DEBUG)

async def go():
    while True:
        data = await router.read()
        print(data)
        router.write(data)

loop = asyncio.get_event_loop()
router = loop.run_until_complete(aiozmq.create_zmq_stream(
    zmq.ROUTER,
    bind='tcp://127.0.0.1:9875'))

loop.run_until_complete(go())
router.close()
print("DONE")

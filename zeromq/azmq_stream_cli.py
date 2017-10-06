import asyncio
import aiozmq
import zmq


async def go():
    for i in range(10):
        msg = (b'data', b'ask', str(i).encode('utf-8'))
        dealer.write(msg)
        answer = await dealer.read()
        print(answer)


loop = asyncio.get_event_loop()
dealer = loop.run_until_complete(aiozmq.create_zmq_stream(
    zmq.DEALER,
    connect='tcp://127.0.0.1:9875'))

loop.run_until_complete(go())
print("DONE")

dealer.close()

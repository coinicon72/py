import os, io, asyncio


class Server(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.peer = None

    def connection_made(self, transport):
        peer = transport.get_extra_info('peername')
        print('connected:', peer)
        self.transport = transport
        self.peer = peer

    def data_received(self, data):
        message = data.decode().rstrip()
        print('{}: {}', self.peer, message)

        if message == 'bye':
            self._close()

    def error_received(self, exc):
        print('error:', exc)

    def connection_lost(self, exc):
        print('disconnected: ', self.peer)
        # self._close()

    def _close(self):
        self.transport.close()
        # loop = asyncio.get_event_loop()
        # loop.stop()


loop = asyncio.get_event_loop()
coro = loop.create_server(Server, '', 6789)
server = loop.run_until_complete(coro)
print('serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

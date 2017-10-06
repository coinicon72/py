"""
will run two tasks
one for tcp client to connect to server and exchange packets
one for stdin to get user's input and send it to server
"""
import os, io, asyncio


class Client(asyncio.Protocol):
    def __init__(self, loop):
        self.transport = None
        self.loop = loop

    def connection_made(self, transport):
        print('connected')
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print(message)

    def error_received(self, exc):
        print('error:', exc)

    def connection_lost(self, exc):
        print('disconnected')
        self._close()

    def _close(self):
        self.transport.close()
        self.loop.stop()


loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: Client(loop), '127.0.0.1', 6789)
trans_sock, _ = loop.run_until_complete(coro)
print('connected to server')

asyncio.wait()

# stdin
class StdIn(asyncio.Protocol):
    def __init__(self, sock):
        self.transport = None
        self.sock = sock

    def data_received(self, data):
        self.sock.write(data)

coro_stdin = loop.connect_read_pipe(lambda: StdIn(trans_sock), io.FileIO(0))
trans_stdin, _ = loop.run_until_complete(coro_stdin)


#
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

loop.close()

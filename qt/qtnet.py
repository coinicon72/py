import sys, uuid
from qtpy.QtCore import QCoreApplication, QObject, Signal, Slot
from qtpy.QtNetwork import QTcpServer, QTcpSocket, QHostAddress


EOL = '\r\n'

class Client(QObject):
    def __init__(self, server, socket, parent=None):
        super(Client, self).__init__(parent)

        self.id = uuid.uuid4().int
        self.name = None

        self.server = server

        self.socket = socket
        self.socket.connected.connect(self._connected)
        self.socket.readyRead.connect(self._onMessage)
        self.socket.disconnected.connect(self._disconnected)
        self.socket.error.connect(self._error)

        self.socket.writeData(b"Hi, what's your name? ")
        self.socket.flush()

    def _send(self, msg):
        """msg is string"""
        self.socket.writeData(msg.encode())
        self.socket.flush()

    def _send_line(self, msg):
        """msg is string"""
        self._send(msg + EOL)

    @Slot()
    def _connected(self):
        print('client: connected from', self.socket.peerAddress())

    def _onMessage(self):
        size =  self.socket.bytesAvailable()
        if size > 0:
            data = self.socket.readAll()
            msg = data.data().decode()
            msg = msg.rstrip()
            print('\treceived:', msg)

            if len(msg) <=0:
                return

            if self.name is None:
                self.name = msg
                self._send_line('[SYS] Welcome, {}.'.format(msg))

                self.server.client_registered.emit(self)
            else:
                if msg == 'bye':
                    self.socket.close()
                else:
                    self.server.client_message.emit(self, msg)

    @Slot()
    def _disconnected(self):
        print('client: disconnected')
        self.server.client_disconnected.emit(self)

    def _error(self, err=None):
        print('client: error ', err)


class Server(QObject):
    client_registered = Signal(Client)
    client_message = Signal(Client, str)
    client_disconnected = Signal(Client)

    def __init__(self, parent=None):
        super(Server, self).__init__(parent)

        self.server = None
        self.clients = {}

        self.client_registered.connect(self.on_client_registered)
        self.client_message.connect(self.on_client_message)
        self.client_disconnected.connect(self.on_client_disconnected)

    def _broad_cast(self, msg):
        """msg is string"""
        data = msg.encode()
        for c in self.clients.values():
            c.socket.writeData(data)
            c.socket.flush()

    def _broad_cast_line(self, msg):
        """msg is string"""
        self._broad_cast(msg + EOL)

    @Slot()
    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        print('server: connected from {}:{}'.format(socket.peerAddress().toString(), socket.peerPort()))

        # self.clients[socket.peerAddress()] = Client(socket)
        #
        # socket.writeData(b"Hi, what's your name?")
        # socket.flush()
        c = Client(self, socket)
        self.clients[c.id] = c

    @Slot(Client)
    def on_client_registered(self, client):
        self._broad_cast_line('[SYS] {} arrived.'.format(client.name))

    @Slot(Client, str)
    def on_client_message(self, client, msg):
        self._broad_cast_line('{}: {}'.format(client.name, msg))

    @Slot(Client)
    def on_client_disconnected(self, client):
        print("server: client disconnected", client.socket.peerAddress().toString(), client.socket.peerPort())
        self._broad_cast_line('[SYS] {} leaved.'.format(client.name))
        del self.clients[client.id]

    def start(self):
        self.server = QTcpServer()
        if self.server.listen(QHostAddress(''), 56682):
            print('server: listening ...')
            self.server.newConnection.connect(self.on_new_connection)
        else:
            print('server: failed to start tcp server')
            self.server.close()

        return self

# def on_new_connection():
#     print('new connection')
#     client = server.nextPendingConnection()
#     print('connected from', client.peerAddress())
#     pass

if __name__ == '__main__':
    app = QCoreApplication(sys.argv)

    # server = QTcpServer(app)
    # if server.listen(QHostAddress(''), 9876):
    #     print('listening ...')
    # else:
    #     print('failed to start tcp server')
    #     sys.exit(-1)
    # # server = Server()
    # # server.start()
    # server.newConnection.connect(on_new_connection)

    server = Server().start()

    sys.exit(app.exec())

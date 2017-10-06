from qtpy.QtCore import QCoreApplication, QObject, Signal, Slot, Property, QUrl
# from qtpy.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *


class BackEnd(QObject):
    onNameChanged = Signal()

    def __init__(self, parent=None):
        super(BackEnd, self).__init__(parent)
        self._name = None

    @Property(str)
    def userName(self):
        return self._name

    @userName.setter
    def userName(self, name):
        self._name = name
        self.onNameChanged.emit()


if __name__ == '__main__':
    app = QCoreApplication([''])
    eng = QQmlApplicationEngine()

    qmlRegisterType(BackEnd, 'qml.backend', 1, 0, 'BackEnd')

    eng.load('app.qml')

    app.exec()


def test1_view():
    app = QCoreApplication([''])

    app.exec()

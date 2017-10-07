import sys, logging
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    source = QUrl().fromLocalFile('color_picker.qml')

    widget = QQuickView()
    widget.setSource(source)
    widget.show()

    # widget.engine().quit.connect(app.quit)

    sys.exit(app.exec())

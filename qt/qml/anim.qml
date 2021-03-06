import QtQuick 2.6

Rectangle {
    id: page
    width: 320; height: 480
    color: "lightgray"

    Text {
        id: helloText
        text: "Hello world!"
        y: 30
        anchors.horizontalCenter: page.horizontalCenter
        font.pointSize: 24; font.bold: true

        MouseArea { id: mouseArea; anchors.fill: parent }

        states: State {
            name: "down"; when: mouseArea.pressed == true
            PropertyChanges { target: helloText; y: 160; rotation: 180; color: "red" }
        }

        transitions: Transition {
            from: ""; to: "down"; reversible: true
            ParallelAnimation {
                NumberAnimation { properties: "y,rotation"; duration: 500; easing.type: Easing.InOutQuad }
                ColorAnimation { duration: 500 }
            }
        }
    }

    Text {
        id: text1
        x: 88
        text: qsTr("↑↑ Click this one ↑↑")
        anchors.horizontalCenter: helloText.horizontalCenter
        anchors.top: helloText.bottom
        anchors.topMargin: 20
        font.pixelSize: 12
    }

}

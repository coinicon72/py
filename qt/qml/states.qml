import QtQuick 2.0
import QtQuick.Controls 1.3

Item {
    id: wnd
    width: 640
    height: 480

    Rectangle {
        id: rectangle
        x: 8
        y: 8
        width: 624
        height: 464
        color: "#877ae1"

        Button {
            id: button
            x: 89
            y: 433
            text: qsTr("Button")
//            onReleased: wnd.state = 'State1'
            onClicked: wnd.state = 'State1'
        }

        Button {
            id: button1
            x: 8
            y: 433
            text: qsTr("Button")
        }
    }

    Rectangle {
        id: rectangle1
        width: 200
        height: 200
        color: "#ffffff"
        visible: false
        opacity: 0

        Button {
            id: button2
            text: qsTr("Button")
            opacity: 0
        }

        Button {
            id: button3
            text: qsTr("Button")
            opacity: 0
//            onReleased: wnd.state = 'State2'
            onClicked: wnd.state = 'State2'
        }
    }
    states: [
        State {
            name: "State1"

            PropertyChanges {
                target: rectangle1
                x: 8
                y: 8
                width: 624
                height: 464
                color: "#b6eed5"
                visible: true
                opacity: 1
            }

            PropertyChanges {
                target: rectangle
                visible: false
            }

            PropertyChanges {
                target: button2
                x: 46
                y: 140
                opacity: 1
            }

            PropertyChanges {
                target: button3
                x: 46
                y: 191
                opacity: 1
            }
        },
        State {
            name: "State2"
        }
    ]

}

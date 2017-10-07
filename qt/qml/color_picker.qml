import QtQuick 2.6
//import QtQuick.Window 2.2

//Window {
//    visible: true
//    width: 640
//    height: 480
//    title: qsTr("Hello World")

//    MouseArea {
//        anchors.fill: parent
//        onClicked: {
//            console.log(qsTr('Clicked on background. Text: "' + textEdit.text + '"'))
//        }
//    }

//    TextEdit {
//        id: textEdit
//        text: qsTr("Enter some text...")
//        verticalAlignment: Text.AlignVCenter
//        anchors.top: parent.top
//        anchors.horizontalCenter: parent.horizontalCenter
//        anchors.topMargin: 20
//        Rectangle {
//            anchors.fill: parent
//            anchors.margins: -10
//            color: "transparent"
//            border.width: 1
//        }
//    }
//}


Rectangle {
    id: page
    width: 500; height: 200
    color: "lightgray"

    Text {
        id: helloText
        text: "Hello world!"
        y: 30
        anchors.horizontalCenter: page.horizontalCenter
        font.pointSize: 24; font.bold: true

//        MouseArea { id: mouseArea; anchors.fill: parent }

//        states: State {
//            name: "down"; when: mouseArea.pressed === true
//            PropertyChanges { target: helloText; y: 160; rotation: 180; color: "red" }
//        }

//        transitions: Transition {
//            from: ""; to: "down"; reversible: true
//            ParallelAnimation {
//                NumberAnimation { properties: "y,rotation"; duration: 500; easing.type: Easing.InOutQuad }
//                ColorAnimation { duration: 500 }
//            }
//        }
    }

    Grid {
        id: colorPicker
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 4
        anchors.left: parent.left; anchors.leftMargin: 4; //; height: 50; width: 100
        rows: 2; columns: 3; spacing: 3

//        Rectangle {
//            color: "red"

//            MouseArea { onClicked: helloText.color = parent.color }
//        }

//        Rectangle {
//            color: "green"

//            MouseArea { onClicked: helloText.color = parent.color }
//        }

//        MouseArea { color: "red"; onClicked: helloText.color = color }
//        MouseArea { color: "green"; onClicked: helloText.color = color }
//        MouseArea { color: "blue"; onClicked: helloText.color = color }
//        MouseArea { color: "yellow"; onClicked: helloText.color = color }
//        MouseArea { color: "steelblue"; onClicked: helloText.color = color }
//        MouseArea { color: "black"; onClicked: helloText.color = color }

        Cell { cellColor: "white"; onClicked: helloText.color = cellColor }
        Cell { cellColor: "green"; onClicked: helloText.color = cellColor }
        Cell { cellColor: "blue"; onClicked: helloText.color = cellColor }
        Cell { cellColor: "yellow"; onClicked: helloText.color = cellColor }
        Cell { cellColor: "steelblue"; onClicked: helloText.color = cellColor }
        Cell { cellColor: "black"; onClicked: helloText.color = cellColor }
    }
}

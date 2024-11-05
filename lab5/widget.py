from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, text) -> None:
        '''
        setup UI on QDialogMessage and connect "ok" button
        :param Form: object QDialogMessage
        :param text: text on QDialogMessage
        :return: None
        '''
        Form.text = text
        Form.setObjectName("Form")
        Form.resize(200, 100)
        Form.setStyleSheet("\n"
"background-color: rgb(31, 167, 110);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -1, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMargin(30)
        self.label.setObjectName("label")
        self.dialogButton = QtWidgets.QPushButton(Form)
        self.dialogButton.setGeometry(QtCore.QRect(50, 50, 93, 28))
        self.dialogButton.setStyleSheet("background-color: rgb(41, 143, 36);\n"
"color:rgb(28, 32, 113)")
        self.dialogButton.setObjectName("dialogButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.dialogButton.clicked.connect(Form.close)

    def retranslateUi(self, Form) -> None:
        '''
        Retranslate objects on QDialogMessage
        :param Form: object QDialogMessage
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", Form.text))
        self.dialogButton.setText(_translate("Form", "ok"))

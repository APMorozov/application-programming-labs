from imgiterator import ImgIterator
from widget import Ui_Form

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow) -> None:
        '''
        setup UI mainWindow abd connect 2 buttons "NEXT" and "ADD"
        :param MainWindow: object QMainWindow
        :return: None
        '''
        self.annotationPath = ""
        self.counter = 0
        self.iterator = None


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(31, 167, 110);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.label_top.setMargin(350)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)


        self.label_top.setFont(font)
        self.label_top.setStyleSheet("color:rgb(28, 32, 113)")
        self.label_top.setScaledContents(False)
        self.label_top.setWordWrap(False)
        self.label_top.setObjectName("label_top")


        self.next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.next_Button.setGeometry(QtCore.QRect(611, 440, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)


        self.next_Button.setFont(font)
        self.next_Button.setStyleSheet("background-color: rgb(41, 143, 36);\n"
"color:rgb(28, 32, 113)")
        self.next_Button.setObjectName("next_Button")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(-1, 440, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)


        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(41, 143, 36);\n"
"color:rgb(28, 32, 113)")


        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(0, 40, 801, 401))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("start_img.jpg"))
        self.label_img.setObjectName("label_img")
        self.label_img.setScaledContents(True)


        self.inpt_path = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inpt_path.setGeometry(QtCore.QRect(190, 510, 351, 41))
        self.inpt_path.setStyleSheet("background-color: rgb(41, 143, 36);\n"
"color:rgb(28, 32, 113)")
        self.inpt_path.setObjectName("inpt_path")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(190, 470, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)


        self.label_path.setFont(font)
        self.label_path.setStyleSheet("color:rgb(28, 32, 113)")
        self.label_path.setObjectName("label_path")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(41, 143, 36);\n"
"color:rgb(28, 32, 113)")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: self.take_csvpath())
        self.next_Button.clicked.connect(lambda: self.take_next(self.annotationPath))

    def retranslateUi(self, MainWindow) -> None:
        '''
        Retranslate objects on MainWindow
        :param MainWindow: object QMainWindow
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_top.setText(_translate("MainWindow", "IMAGE"))
        self.next_Button.setText(_translate("MainWindow", "NEXT"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.inpt_path.setPlainText(_translate("MainWindow", "Input"))
        self.label_path.setText(_translate("MainWindow", "Input PATH to annotation"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))

    def take_next(self, path) -> None:
        '''
        Take next img to app
        :param path: PATH to annotation
        :return: None
        '''
        if self.counter == 0:
            print("PATH", path)
            print('Инициализация итератора...')
            try:
                self.iterator = ImgIterator(path)
                iter(self.iterator)
            except Exception as ex:
                print("Init iterator error", ex)
                widget = QtWidgets.QDialog()
                wid = Ui_Form()
                wid.setupUi(widget, 'Wrong PATH')
                widget.exec_()
                return


            try:
                 imgPath = next(self.iterator)
                 print("Путь:", imgPath[1])
                 self.label_img.setPixmap(QtGui.QPixmap(imgPath[1]))
                 self.counter += 1
            except StopIteration:
                print("No more img")
                widget = QtWidgets.QDialog()
                wid = Ui_Form()
                wid.setupUi(widget, 'No more img')
                widget.exec_()
            except Exception as ex:
                 print(ex)
        else:
            try:
                print('caras')
                imgPath = next(self.iterator)
                print("es&", imgPath[1])
                self.label_img.setPixmap(QtGui.QPixmap(imgPath[1]))
            except StopIteration:
                print("No more img")
                widget = QtWidgets.QDialog()
                wid = Ui_Form()
                wid.setupUi(widget, 'No more img')
                widget.exec_()
            except Exception as ex:
                print(ex)
                widget = QtWidgets.QDialog()
                wid = Ui_Form()
                wid.setupUi(widget, 'Error')
                widget.exec_()

    def take_csvpath(self) -> None:
        '''
        Take path to csv from Qlable
        :return: None
        '''
        path = self.inpt_path.toPlainText()
        self.annotationPath = path
        self.counter = 0
        widget = QtWidgets.QDialog()
        wid = Ui_Form()
        wid.setupUi(widget, 'PATH was add')
        widget.exec_()



def main():
    try:
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        ui.exitButton.clicked.connect(lambda: sys.exit(app.exec_()))
        sys.exit(app.exec_())
    except Exception as ex:
        print("Error in main:", ex)


if __name__ == '__main__':
    main()

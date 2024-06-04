from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 489)
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.label_3.setStyleSheet("background-image: url(:/images/a13f7a5fa480580ff92490c56eac05c5.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 321, 491))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 500))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,150);\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(770, 0, 22, 481))
        self.verticalSlider.setStyleSheet("QSlider::groove:vertical{\n"
"background-color:rgba(0,0,0,0);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"width:10px;\n"
"height:30px;\n"
"padding:5px;\n"
"background-color:rgba(255,33,100,230);\n"
"border-radius:10px;\n"
"}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 321, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setStyleSheet("QListWidget{\n"
"background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(255,33,100,230);\n"
"border-radius:10px;\n"
"padding:10px;\n"
"font-size:15pt;\n"
"color:rgba(255,255,255,200);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(255,33,100,230);\n"
"border-radius:10px;\n"
"padding:10px;\n"
"font-size:15pt;\n"
"color:rgba(255,255,255,200);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,33,100,100);\n"
"}")
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.widget1)
        self.widget2 = QtWidgets.QWidget(self.widget)
        self.widget2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.widget2.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(255,33,100,230);\n"
"border-radius:10px;\n"
"padding:10px;\n"
"font-size:15pt;\n"
"color:rgba(255,255,255,200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,33,100,100);\n"
"}")
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.verticalLayout.addWidget(self.widget2)
        self.widget.raise_()
        self.widget.raise_()
        self.listWidget.raise_()
        self.label_3.raise_()
        self.verticalSlider.raise_()
        self.label_2.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_5.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_3.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", "START"))
        self.pushButton_4.setText(_translate("MainWindow", ">"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow
from pygame import mixer
import unterface


class Player(QWidget, unterface.Ui_MainWindow):

    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)

        self.setFixedSize(self.size())

        self.pushButton_2.clicked.connect(self.play)
        self.pushButton_3.clicked.connect(self.prev)
        self.pushButton_4.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_5.clicked.connect(self.remove)

        self.listWidget.doubleClicked.connect(self.play)

        self.dir=""
        self.soundMixer = mixer
        self.soundMixer.init()

    def play(self):
        item = self.listWidget.currentItem()

        if item:
            filename = os.path.join(self.dir, item.text())
            self.soundMixer.music.load(filename)
        else:
            self.listWidget.currentRow(0)
        self.soundMixer.music.play()

    def prev(self):
        pass

    def next(self):
        pass

    def add(self):
        self.listWidget.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select dir")

        if dir:
            for filename in os.listdir(dir):
                if filename.endswith(".mp3") or filename.endswith(".wav"):
                    self.listWidget.addItem(os.path.join(filename))
        self.dir = dir

    def remove(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
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

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(50)
        self.verticalSlider.valueChanged.connect(self.volume)

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
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row - 1)
            self.play()
        except TypeError:
            pass

    def next(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row + 1)
            self.play()
        except TypeError:
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
        self.listWidget.clear()
        self.sound_mixer.music.stop()

    def volume(self):
        self.soundMixer.music.set_volume(self.verticalSlider.value()/100)

app = QtWidgets.QApplication(sys.argv)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
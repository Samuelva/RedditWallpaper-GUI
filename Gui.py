#!/usr/bin/python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Wallpaper import Wallpaper
#from PyQt5.QtWidgets import QMainWindow, QWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, Wallpaper):
        super(MainWindow, self).__init__()
        self.Wallpaper = Wallpaper
        parameters = Parameters(self, self.Wallpaper)
        preview = Preview(self, self.Wallpaper)
        navigation = Navigation(self, self.Wallpaper)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(parameters)
        self.mainLayout.addWidget(preview)
        self.mainLayout.addWidget(navigation)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.centralWidget)

        self.setWindowTitle("Reddit Wallpaper")
        self.show()


class Parameters(QtWidgets.QFrame):
    def __init__(self, parent, Wallpaper):
        super(Parameters, self).__init__(parent=parent)
        self.Wallpaper = Wallpaper
        #self.setFrameShape(QtWidgets.QFrame.Panel)

        # pBox = QtWidgets.QHBoxLayout()

        # pLabels = QtWidgets.QVBoxLayout()

        # pLabels.addWidget(QtWidgets.QLabel("Subreddit", self))
        # pLabels.addWidget(QtWidgets.QLabel("Submission", self))
        # pLabels.addWidget(QtWidgets.QLabel("Resolution", self))

        self.subInput = QtWidgets.QLineEdit("Wallpaper", self)
        self.subInput.textChanged.connect(self.inputChange)
        self.subInput.setToolTip("Set the subreddit")

        self.comboSub = QtWidgets.QComboBox(self)
        self.comboSub.addItem("Day")
        self.comboSub.addItem("Week")
        self.comboSub.addItem("Month")
        self.comboSub.addItem("Year")
        self.comboSub.addItem("All")
        self.comboSub.setToolTip("Set the type of submission")
        self.comboSub.currentIndexChanged.connect(self.submissionChange)

        self.comboRes = QtWidgets.QComboBox(self)
        self.comboRes.addItem("1920x1080")
        self.comboRes.addItem("1366x768")
        self.comboRes.addItem("1280x1024")
        self.comboRes.addItem("800x600")
        self.comboRes.setToolTip("Set the resolution")
        self.comboRes.currentIndexChanged.connect(self.resolutionChange)

        self.previewBtn = QtWidgets.QPushButton("GO", self)
        self.previewBtn.setFixedWidth(35)
        self.previewBtn.setToolTip("Retrieve and preview the wallpapers") 
        
        pSelection = QtWidgets.QHBoxLayout()
        pSelection.addWidget(self.subInput)
        pSelection.addWidget(self.comboSub)
        pSelection.addWidget(self.comboRes)
        pSelection.addWidget(self.previewBtn)
        pSelection.setContentsMargins(2, 0, 2, 0)

        # pBox.addLayout(pLabels)
        #pBox.addLayout(pSelection)
        #self.setLayout(pBox)
        self.setFixedHeight(40)
        self.setLayout(pSelection)

    def inputChange(self, subreddit):
        self.Wallpaper.subreddit = subreddit


    def submissionChange(self):
        self.Wallpaper.submission = self.comboSub.currentText()


    def resolutionChange(self):
        self.Wallpaper.resolution = self.comboRes.currentText()


class Preview(QtWidgets.QFrame):
    def __init__(self, parent, Wallpaper):
        super(Preview, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.Panel)

        previewPM = QtGui.QPixmap("JdbvxK6.jpg")
        previewPM = previewPM.scaled(384, 216)
        lbl = QtWidgets.QLabel(self)
        lbl.setPixmap(previewPM)

        pLabel = QtWidgets.QVBoxLayout()
        pLabel.addWidget(lbl)
        pLabel.setContentsMargins(0, 0, 0, 0)
        self.setLayout(pLabel)


class Navigation(QtWidgets.QFrame):
    def __init__(self, parent, Wallpaper):
        super(Navigation, self).__init__()
        self.wallpaper = Wallpaper
        
        self.prevBtn = QtWidgets.QPushButton("<", self)
        self.changeBtn = QtWidgets.QPushButton("O", self)
        self.changeBtn.setToolTip("Change your wallpaper")
        self.changeBtn.setFixedWidth(35)
        self.nextBtn = QtWidgets.QPushButton(">", self)

        nBox = QtWidgets.QHBoxLayout()
        nBox.addWidget(self.prevBtn)
        nBox.addWidget(self.changeBtn)
        nBox.addWidget(self.nextBtn)

        self.setLayout(nBox)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow(Wallpaper())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
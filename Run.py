#!/usr/bin/python

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Wallpaper import Wallpaper
#from PyQt5.QtWidgets import QMainWindow, QWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, Wallpaper):
        super(MainWindow, self).__init__()
        self.setUp(Wallpaper, "JdbvxK6.jpg")
        self.setWindowTitle("Reddit Wallpaper")
    
    def setUp(self, Wallpaper, image):
        self.Wallpaper = Wallpaper
        self.parameters = Parameters(self, self.Wallpaper)
        self.preview = Preview(self, self.Wallpaper, image)
        # self.navigation = Navigation(self, self.Wallpaper)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.parameters)
        self.mainLayout.addWidget(self.preview)
        # self.mainLayout.addWidget(self.navigation)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.show()


class Parameters(QtWidgets.QFrame):
    def __init__(self, parent, Wallpaper):
        super(Parameters, self).__init__(parent=parent)
        self.Wallpaper = Wallpaper

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
        self.comboRes.addItem("Any")
        self.comboRes.addItem("1920x1080")
        self.comboRes.addItem("1366x768")
        self.comboRes.addItem("1280x1024")
        self.comboRes.addItem("800x600")
        self.comboRes.setToolTip("Set the resolution")
        self.comboRes.currentIndexChanged.connect(self.resolutionChange)

        self.previewBtn = QtWidgets.QPushButton("GO", self)
        self.previewBtn.setFixedWidth(35)
        self.previewBtn.setToolTip("Retrieve and preview the wallpapers") 
        self.previewBtn.clicked.connect(self.showPreview)
        
        pSelection = QtWidgets.QHBoxLayout()
        pSelection.addWidget(self.subInput)
        pSelection.addWidget(self.comboSub)
        pSelection.addWidget(self.comboRes)
        pSelection.addWidget(self.previewBtn)
        pSelection.setContentsMargins(2, 0, 2, 0)

        self.setFixedHeight(40)
        self.setLayout(pSelection)

    def inputChange(self, subreddit):
        print(subreddit)
        self.Wallpaper.subreddit = subreddit

    def submissionChange(self):
        print(self.comboSub.currentText())
        self.Wallpaper.submission = self.comboSub.currentText()

    def resolutionChange(self):
        print(self.comboRes.currentText())
        self.Wallpaper.resolution = self.comboRes.currentText()

    def showPreview(self):
        self.Wallpaper.getWallpapers()


class Preview(QtWidgets.QWidget):
    def __init__(self, parent, Wallpaper, image):
        super(Preview, self).__init__()
        self.wallpaper = Wallpaper
        # self.setFrameShape(QtWidgets.QFrame.Panel)
        # previewFrame = QtWidgets.QFrame()
        # previewFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.previewPM = QtGui.QPixmap(image)
        self.previewPM = self.previewPM.scaled(384, 216)
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setPixmap(self.previewPM)
        self.lbl.show()

        previewPMBox = QtWidgets.QVBoxLayout()
        previewPMBox.addWidget(self.lbl)

        self.prevBtn = QtWidgets.QPushButton("<", self)
        self.changeBtn = QtWidgets.QPushButton("O", self)
        self.changeBtn.setToolTip("Change your wallpaper")
        self.changeBtn.setFixedWidth(35)
        self.nextBtn = QtWidgets.QPushButton(">", self)

        self.prevBtn.clicked.connect(self.prevButton)
        self.nextBtn.clicked.connect(self.nextButton)
        self.changeBtn.clicked.connect(self.changeButton)

        navigationBox = QtWidgets.QHBoxLayout()
        navigationBox.addWidget(self.prevBtn)
        navigationBox.addWidget(self.changeBtn)
        navigationBox.addWidget(self.nextBtn)
        navigationBox.setContentsMargins(5, 2, 5, 0)

        self.disableNavButton()

        previewBox = QtWidgets.QVBoxLayout()
        previewBox.addLayout(previewPMBox)
        previewBox.addLayout(navigationBox)
        # pLabel = QtWidgets.QVBoxLayout()
        previewBox.setContentsMargins(2, 0, 2, 0)
        self.setLayout(previewBox)
    
    def pixmap(self, image):
        self.previewPM = QtGui.QPixmap(image)
        self.previewPM = self.previewPM.scaled(384, 216)
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setPixmap(self.previewPM)
        self.lbl.show()

    def prevButton(self):
        self.wallpaper.imageIndex -= 1
        self.disableNavButton()
        test = QtGui.QPixmap(self.wallpaper.imageList[self.wallpaper.imageIndex])
        test = test.scaled(384, 216)
        self.lbl.setPixmap(test)

    def nextButton(self):
        self.wallpaper.imageIndex += 1
        self.disableNavButton()
        test = QtGui.QPixmap(self.wallpaper.imageList[self.wallpaper.imageIndex])
        test = test.scaled(384, 216)
        self.lbl.setPixmap(test)

    def changeButton(self):
        print("/home/samuel/Documents/RedditWallpaper-GUI"+self.wallpaper.imageList[self.wallpaper.imageIndex])
        os.system("gsettings set org.gnome.desktop.background picture-uri file://%(path)s" % {'path':"/home/samuel/Documents/RedditWallpaper-GUI/"+self.wallpaper.imageList[self.wallpaper.imageIndex]})
        os.system("gsettings set org.gnome.desktop.background picture-options wallpaper")

    def disableNavButton(self):
        imageIndex = self.wallpaper.imageIndex
        print(imageIndex)

        if imageIndex == 0:
            self.prevBtn.setEnabled(False)
        elif imageIndex > 0:
            self.prevBtn.setEnabled(True)
        
        if imageIndex == len(self.wallpaper.imageList)-1:
            self.nextBtn.setEnabled(False)
        elif imageIndex < len(self.wallpaper.imageList)-1:
            self.nextBtn.setEnabled(True)


# class Navigation(QtWidgets.QFrame):
#     def __init__(self, parent, Wallpaper):
#         super(Navigation, self).__init__()
#         self.wallpaper = Wallpaper
        
#         self.prevBtn = QtWidgets.QPushButton("<", self)
#         self.changeBtn = QtWidgets.QPushButton("O", self)
#         self.changeBtn.setToolTip("Change your wallpaper")
#         self.changeBtn.setFixedWidth(35)
#         self.nextBtn = QtWidgets.QPushButton(">", self)

#         self.prevBtn.clicked.connect(self.prevButton)
#         self.nextBtn.clicked.connect(self.nextButton)

#         nBox = QtWidgets.QHBoxLayout()
#         nBox.addWidget(self.prevBtn)
#         nBox.addWidget(self.changeBtn)
#         nBox.addWidget(self.nextBtn)

#         self.setLayout(nBox)

#     def prevButton(self):
#         print("prev lel")

#     def nextButton(self):
#         print("next kek")
#         self.Preview.lbl.setPixmap("q7Zf6yM.jpg")
#         Preview.lbl.show()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow(Wallpaper())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
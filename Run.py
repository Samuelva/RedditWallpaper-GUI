#!/usr/bin/python

import ctypes
import os
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Wallpaper import Wallpaper

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, Wallpaper):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon("Pictogram2.png"))
        self.wallpaper = Wallpaper
        self.parameters = Parameters(self, self.wallpaper)
        self.preview = Preview(self, self.wallpaper)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.parameters)
        self.mainLayout.addWidget(self.preview)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle("Reddit Wallpaper")

        self.show()

    def closeEvent(self, event):
        self.wallpaper.delete()
        event.accept()

class Parameters(QtWidgets.QFrame):
    def __init__(self, parent, Wallpaper):
        super(Parameters, self).__init__(parent=parent)
        self.parent = parent
        self.wallpaper = Wallpaper

        self.subInput = QtWidgets.QLineEdit("Wallpapers", self)
        self.subInput.textChanged.connect(self.inputChange)
        self.subInput.setToolTip("Set the subreddit")

        self.comboSub = QtWidgets.QComboBox(self)
        self.comboSub.addItem("Day")
        self.comboSub.addItem("Week")
        self.comboSub.addItem("Month")
        self.comboSub.addItem("Year")
        self.comboSub.addItem("All")
        self.comboSub.setToolTip("Set the type of submission")
        self.comboSub.setFixedWidth(75)
        self.comboSub.currentIndexChanged.connect(self.submissionChange)

        self.comboRes = QtWidgets.QComboBox(self)
        self.comboRes.addItem("Any")
        self.comboRes.addItem("1920x1080")
        self.comboRes.addItem("1366x768")
        self.comboRes.addItem("1280x1024")
        self.comboRes.addItem("800x600")
        self.comboRes.setToolTip("Set minimum resolution")
        self.comboRes.setFixedWidth(75)
        self.comboRes.currentIndexChanged.connect(self.resolutionChange)

        self.pathBtn = QtWidgets.QPushButton("...")
        self.pathBtn.setToolTip("Specificy location for the wallpapers")
        self.pathBtn.setFixedWidth(35)
        self.pathBtn.clicked.connect(self.inputPath)

        self.previewBtn = QtWidgets.QPushButton("GO", self)
        self.previewBtn.setFixedWidth(35)
        self.previewBtn.setToolTip("Retrieve and preview the wallpapers") 
        self.previewBtn.clicked.connect(self.showPreview)

        # self.testKnopje = QtWidgets.QPushButton("Kek", self)
        # self.testKnopje.setFixedWidth(35)
        # self.testKnopje.setFixedHeight(25)
        # self.testKnopje.clicked.connect(self.testje)
        
        pSelection = QtWidgets.QHBoxLayout()
        pSelection.addWidget(self.subInput)
        pSelection.addWidget(self.comboSub)
        pSelection.addWidget(self.comboRes)
        pSelection.addWidget(self.pathBtn)
        pSelection.addWidget(self.previewBtn)
        # pSelection.addWidget(self.testKnopje)
        pSelection.setContentsMargins(2, 0, 2, 0)

        self.setFixedHeight(40)
        self.setLayout(pSelection)

    # def testje(self):
    #     print(self.wallpaper.savedir)
        # print("\nImage list")
        # print(self.wallpaper.imageList)
        # print("\nImage urls")
        # print(self.wallpaper.imageUrls)
        # print("\nDownloaded")
        # print(self.wallpaper.downloaded)
        # print("\n")

    def inputChange(self, subreddit):
        self.wallpaper.subreddit = subreddit

    def submissionChange(self):
        self.wallpaper.submission = self.comboSub.currentText()

    def resolutionChange(self):
        self.wallpaper.resolution = self.comboRes.currentText()

    def inputPath(self):
        self.wallpaper.savedir = QtWidgets.QFileDialog.getExistingDirectory(self, options=QtWidgets.QFileDialog.ShowDirsOnly)
        if self.wallpaper.savedir == "":
            self.wallpaper.savedir = os.getcwd()

    def showPreview(self):
        self.wallpaper.getSubmissions()
        # print(self.wallpaper.imageUrls)
        self.wallpaper.getWallpapers()
        self.wallpaper.download()
        # print(self.wallpaper.imageList)
        # print(self.wallpaper.imageUrls)
        self.parent.preview.pixmap(self.wallpaper.savedir + "/" + self.wallpaper.imageList[self.wallpaper.imageIndex])
        self.parent.preview.nextBtn.setEnabled(True)
        self.parent.preview.prevBtn.setEnabled(False)

class Preview(QtWidgets.QWidget):
    def __init__(self, parent, Wallpaper):
        super(Preview, self).__init__()
        self.parent = parent
        self.wallpaper = Wallpaper
        self.lbl = QtWidgets.QLabel(self)
        self.loadingLbl = QtWidgets.QLabel(self)
        self.pixmap("Default.jpg") 

        previewPMBox = QtWidgets.QVBoxLayout()
        previewPMBox.addStretch(1)
        previewPMBox.addWidget(self.lbl)
        previewPMBox.addStretch(1)
        # previewPMBox.addWidget(self.loadingLbl)

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

        # self.testKnopje = QtWidgets.QPushButton("Kek", self)
        # self.testKnopje.setFixedWidth(35)
        # self.testKnopje.setFixedHeight(25)
        # self.testKnopje.clicked.connect(self.testje)

        self.disableNavButton()

        previewBox = QtWidgets.QVBoxLayout()
        previewBox.addLayout(previewPMBox)
        previewBox.addLayout(navigationBox)
        previewBox.setContentsMargins(2, 0, 2, 0)
        self.setLayout(previewBox)
    
    def testje(self):
        self.loading()

    def pixmap(self, image):
        self.previewPM = QtGui.QPixmap(image, "1")
        self.previewPM = self.previewPM.scaled(500, 300, QtCore.Qt.KeepAspectRatio)
        self.lbl.setPixmap(self.previewPM)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.show()

    def loading(self):
        effect = QtWidgets.QGraphicsColorizeEffect()
        effect.setColor(QtGui.QColor(0, 0, 0))
        effect.setStrength(0.8)
        # self.lbl.setGraphicsEffect(effect)        
        # self.loadingGif = QtGui.QMovie("squares.gif", QtCore.QByteArray())
        # self.loadingGif.scaledSize()
        # self.loadingGif.setCacheMode(QtGui.QMovie.CacheAll)
        # self.loadingGif.setSpeed(100)
        # self.loadingGif.start()

        # self.loadingLbl.setMovie(self.loadingGif)
        # self.loadingLbl.move(100, 100)
        # self.loadingLbl.show()


    def prevButton(self):
        self.wallpaper.imageIndex -= 1
        self.wallpaper.download()
        self.disableNavButton()
        # print("\n")
        # print(self.wallpaper.imageList[self.wallpaper.imageIndex])
        # print(self.wallpaper.imageUrls[self.wallpaper.imageIndex])
        self.pixmap(self.wallpaper.savedir + "/" + self.wallpaper.imageList[self.wallpaper.imageIndex])

    def nextButton(self):
        self.wallpaper.imageIndex += 1
        self.wallpaper.download()
        self.disableNavButton()
        # print("\n")
        # print(self.wallpaper.imageList[self.wallpaper.imageIndex])
        # print(self.wallpaper.imageUrls[self.wallpaper.imageIndex])
        self.pixmap(self.wallpaper.savedir + "/" + self.wallpaper.imageList[self.wallpaper.imageIndex])

    def changeButton(self):
        self.wallpaper.setWallpaper.append(self.wallpaper.imageList[self.wallpaper.imageIndex])
        if os.name == "posix":
            os.system("gsettings set org.gnome.desktop.background picture-uri file://%(path)s" % {'path':self.wallpaper.savedir + "/" + self.wallpaper.imageList[self.wallpaper.imageIndex]})
            os.system("gsettings set org.gnome.desktop.background picture-options wallpaper")
        elif os.name == "nt":
            path = "C:/Users/Samuel/Dropbox/Projects/RedditWallpaper-GUI/"
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, self.wallpaper.savedir + "/" + self.wallpaper.imageList[self.wallpaper.imageIndex] , 0)
        
    def disableNavButton(self):
        imageIndex = self.wallpaper.imageIndex

        if imageIndex == 0:
            self.prevBtn.setEnabled(False)
        elif imageIndex > 0:
            self.prevBtn.setEnabled(True)
        
        if imageIndex == len(self.wallpaper.imageList)-1:
            self.nextBtn.setEnabled(False)
        elif imageIndex < len(self.wallpaper.imageList)-1:
            self.nextBtn.setEnabled(True)    

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow(Wallpaper())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
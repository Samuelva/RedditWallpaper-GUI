import os
import sys
import wallpaper
from PyQt4 import *
from PyQt4.QtCore import *
import PyQt4
import urllib.request

class GUI(QtGui.QWidget):

    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()


    def initUI(self):
        self.directory = "/home/samuel/Documents/RedditWallpaper-GUI/Wallpapers/"
        self.image_index = 0
        self.downloaded_images = []

        self.test1 = wallpaper.RedditWallpaper("wallpaper")
        self.qle = QtGui.QLineEdit("Wallpaper", self)
        self.qle.move(120, 20)

        lbl1 = QtGui.QLabel("Subreddit:", self)
        lbl1.move(20, 24)

        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Day")
        self.combo.addItem("Week")
        self.combo.addItem("Month")
        self.combo.addItem("Year")
        self.combo.addItem("All Time")
        self.combo.addItem("Database")
        self.combo.currentIndexChanged.connect(self.submissionChange)
        self.combo.move(120, 50)

        lbl2 = QtGui.QLabel("Submission:", self)
        lbl2.move(20, 54)

        self.combo2 = QtGui.QComboBox(self)
        self.combo2.addItem("1920x1080")
        self.combo2.addItem("1366x768")
        self.combo2.addItem("1280x1024")
        self.combo2.addItem("800x600")
        self.combo2.move(120, 80)

        lbl3 = QtGui.QLabel("Resolution:", self)
        lbl3.move(20, 84)

        self.dbChbx = QtGui.QCheckBox("", self)
        self.dbChbx.move(120, 112)
        self.dbChbx.toggle()

        lbl4 = QtGui.QLabel("Save to db:", self)
        lbl4.move(20, 114)

        self.previewOn = False
        self.pBtn = QtGui.QPushButton('Preview', self)
        self.pBtn.setToolTip("Show a preview of the background")
        self.pBtn.resize(self.pBtn.sizeHint())
        self.pBtn.clicked.connect(self.preview)
        self.pBtn.move(120, 140)

        self.cbBtn = QtGui.QPushButton("Change", self)
        self.cbBtn.setToolTip("Change the background")
        self.cbBtn.resize(self.cbBtn.sizeHint())	
        self.cbBtn.clicked.connect(self.change_wallpaper)	
        self.cbBtn.move(210, 140)

        self.setFixedSize(320, 190)
        self.setWindowTitle("Reddit Wallpaper")
        self.show()

        self.lblPixmap = QtGui.QLabel(self)

        self.nextButton = QtGui.QPushButton(">", self)
        self.nextButton.setToolTip("Get the next background")
        self.nextButton.setFixedWidth(30)
        self.nextButton.move(400, 140)

        self.prevButton = QtGui.QPushButton("<", self)
        self.prevButton.setToolTip("Get the previous background")
        self.prevButton.setFixedWidth(30)
        self.prevButton.move(370, 140)


    def submissionChange(self, i):
        if self.combo.currentText() == "Database":
            self.qle.setEnabled(False)
            self.combo2.setEnabled(False)
            self.dbChbx.setEnabled(False)
        else:
            self.qle.setEnabled(True)
            self.combo2.setEnabled(True)
            self.dbChbx.setEnabled(True)
            
    def disableButtons(self):
        if self.image_index+1 == len(self.test1.get_submissions()):
            self.nextButton.setEnabled(False)
        elif self.image_index < len(self.test1.get_submissions()) and self.image_index != 0:
            self.nextButton.setEnabled(True)
            self.prevButton.setEnabled(True)
        elif self.image_index == 0:
            self.prevButton.setEnabled(False)
            
    def preview(self):
        self.image_index = 0
        self.setSubmissions()
        self.disableButtons()
        if not self.previewOn:
            self.previewOn = True
            self.setFixedSize(510, 190)
            self.test1.set_subreddit(self.qle.text())
            self.idknu()
            self.nextButton.show()
            self.prevButton.show()
            self.nextButton.clicked.connect(self.nextImage)
            self.prevButton.clicked.connect(self.prevImage)

        elif self.previewOn:
            self.lblPixmap.hide()
            self.nextButton.hide()
            self.prevButton.hide()
            self.setFixedSize(320, 190)
            self.previewOn = False
    
    def setSubmissions(self):
        if self.combo.currentText() == "Day":
            self.test1.set_submissions_day()
        elif self.combo.currentText() == "Week":
            self.test1.set_submissions_week()
        elif self.combo.currentText() == "Month":
            self.test1.set_submissions_month()
        elif self.combo.currentText() == "Year":
            self.test1.set_submissions_year()
        elif self.combo.currentText() == "All Time":
            self.test1.set_submissions_all_time()
            
    def idknu(self):
        # print(self.image_index)
        # print(self.test1.get_submissions_month()[self.image_index])
        self.test1.set_image(self.directory, 
                             self.test1.get_submissions()[self.image_index].split("/")[-1])
        if self.test1.get_image() not in self.downloaded_images:
            urllib.request.urlretrieve(self.test1.get_submissions()[self.image_index],
                                    self.test1.get_image())
        pixmap = QtGui.QPixmap(self.test1.get_image())
        pixmap2 = pixmap.scaled(200, 110, PyQt4.QtCore.Qt.KeepAspectRatio)
        self.lblPixmap.setPixmap(pixmap2)
        self.lblPixmap.move(320, 20)
        self.lblPixmap.show()

    def nextImage(self):
        self.image_index += 1
        self.disableButtons()
        self.downloaded_images.append(self.test1.get_image())
        self.idknu()

    def prevImage(self):
        self.image_index -= 1
        self.disableButtons()
        self.idknu()

    def change_wallpaper(self):
        os.system("gsettings set org.gnome.desktop.background picture-uri file://%(path)s" % {'path':self.test1.get_image()})
        os.system("gsettings set org.gnome.desktop.background picture-options wallpaper")
    
    # def get

    # def checkUrl(self):


def main():
    app = QtGui.QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
# def main():

# 	app = QtGui.QApplication(sys.argv)

# 	w = QtGui.QWidget()
# 	w.setFixedSize(320, 240)
# 	w.setWindowTitle('Reddit Wallpaper')

# 	@pyqtSlot()
# 	def on_press():
# 		RedditWallpaper.main("-db")

# 	btn = QtGui.QPushButton('Change background', w)
# 	btn.setToolTip('Change background')
# 	btn.clicked.connect(on_press)
# 	btn.resize(btn.sizeHint())
# 	btn.move(100, 80)

# 	w.lbl = QtGui.QLabel("Day", w)
# 	combo = QtGui.QComboBox(w)
# 	combo.addItem("Day")
# 	combo.addItem("Week")
# 	combo.addItem("Month")
# 	combo.addItem("Year")

# 	combo.move(100, 100)
# 	w.lbl.move(100, 100)

# 	combo.activated[str].connect(onActivated(w.lbl, "kek"))


# 	w.show()

# 	exit(app.exec_())

# def onActivated(lbl, text):
# 	lbl.setText(text)
# 	lbl.adjustSize()

# if __name__ == '__main__':
# 	main()


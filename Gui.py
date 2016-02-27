import sys
import RedditWallpaper
import wallpaper
from PyQt4 import *
from PyQt4.QtCore import *
import PyQt4

class GUI(QtGui.QWidget):

	def __init__(self):
		super(GUI, self).__init__()

		self.initUI()

	def initUI(self):

		self.qle = QtGui.QLineEdit("Wallpapers", self)
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
		self.cbBtn.move(210, 140)

		self.setFixedSize(320, 190)
		self.setWindowTitle("Reddit Wallpaper")
		self.show()

	def submissionChange(self, i):
		if self.combo.currentText() == "Database":
			self.qle.setEnabled(False)
			self.combo2.setEnabled(False)
			self.dbChbx.setEnabled(False)
		else:
			self.qle.setEnabled(True)
			self.combo2.setEnabled(True)
			self.dbChbx.setEnabled(True)


	def preview(self):
		if not self.previewOn:
			self.setFixedSize(510, 190)

			pixmap = QtGui.QPixmap("24861344486_b2a2f6805e_k.jpg")
			pixmap2 = pixmap.scaled(200, 110, PyQt4.QtCore.Qt.KeepAspectRatio)

			self.lblPixmap = QtGui.QLabel(self)
			self.lblPixmap.setPixmap(pixmap2)
			self.lblPixmap.move(320, 20)
			self.lblPixmap.show()

			self.previewOn = True
		elif self.previewOn:
			self.setFixedSize(320, 190)
			self.previewOn = False


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


import sys
import RedditWallpaper
import wallpaper
from PyQt4 import *
from PyQt4.QtCore import *

class GUI(QtGui.QWidget):

	def __init__(self):
		super(GUI, self).__init__()

		self.initUI()

	def initUI(self):

		qle = QtGui.QLineEdit("Wallpapers", self)
		qle.move(120, 20)

		lbl1 = QtGui.QLabel("Subreddit:", self)
		lbl1.move(20, 24)

		combo = QtGui.QComboBox(self)
		combo.addItem("Day")
		combo.addItem("Week")
		combo.addItem("Month")
		combo.addItem("Year")
		combo.addItem("All Time")
		combo.addItem("Database")

		combo.move(120, 50)

		lbl2 = QtGui.QLabel("Submission:", self)
		lbl2.move(20, 54)

		# cb = QtGui.QCheckBox("Database",self)
		# cb.move(200, 53)
		# cb.toggle()

		combo2 = QtGui.QComboBox(self)
		combo2.addItem("1920x1080")
		combo2.addItem("1366x768")
		combo2.addItem("1280x1024")
		combo2.addItem("800x600")

		combo2.move(120, 80)

		lbl3 = QtGui.QLabel("Resolution:", self)
		lbl3.move(20, 84)

		dbChbx = QtGui.QCheckBox("", self)
		dbChbx.move(120, 112)
		dbChbx.toggle()

		lbl4 = QtGui.QLabel("Save to db:", self)
		lbl4.move(20, 114)

		pBtn = QtGui.QPushButton('Preview', self)
		pBtn.setToolTip("Show a preview of the background")
		pBtn.resize(pBtn.sizeHint())
		pBtn.clicked.connect(self.handleButton)

		pBtn.move(120, 140)

		cbBtn = QtGui.QPushButton("Change", self)
		cbBtn.setToolTip("Change the background")
		cbBtn.resize(cbBtn.sizeHint())
		
		cbBtn.move(210, 140)


		# btn2 = QtGui.QPushButton("Add to database", self)
		# btn2.setToolTip("Add this background to the database")
		# btn2.resize(btn2.sizeHint())

		# btn2.move(100, 160)



		# hbox = QtGui.QHBoxLayout(self)
		# pixmap = QtGui.QPixmap("24861344486_b2a2f6805e_k.jpg")
		# pixmap2 = pixmap.scaled(192, 108, PyQt4.QtCore.Qt.KeepAspectRatio)
		# lbl2 = QtGui.QLabel(self)
		# lbl2.setPixmap(pixmap2)

		# hbox.addWidget(lbl2)
		# self.setLayout(hbox)

		self.setFixedSize(320, 190)
		self.setWindowTitle("Reddit Wallpaper")
		self.show()

	def handleButton(self):
		self.setFixedSize(500, 190)

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


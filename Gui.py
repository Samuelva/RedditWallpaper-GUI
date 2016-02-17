import sys
import RedditWallpaper
import wallpaper
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
import PyQt4.QtCore


class GUI(QtGui.QWidget):

	def __init__(self):
		super(GUI, self).__init__()

		self.initUI()

	def initUI(self):

		qle = QtGui.QLineEdit("Wallpapers", self)
		qle.move(100, 40)

		combo = QtGui.QComboBox(self)
		combo.addItem("Day")
		combo.addItem("Week")
		combo.addItem("Month")
		combo.addItem("Year")
		combo.addItem("All Time")

		combo.move(100, 80)

		btn = QtGui.QPushButton('Preview', self)
		btn.setToolTip('Change background')
		btn.resize(btn.sizeHint())

		btn.move(100, 120)

		btn2 = QtGui.QPushButton("Add to database", self)
		btn2.setToolTip("Add this background to the database")
		btn2.resize(btn2.sizeHint())

		btn2.move(100, 160)

		cb = QtGui.QCheckBox("Database",self)
		cb.move(200, 80)
		cb.toggle()

		hbox = QtGui.QHBoxLayout(self)
		pixmap = QtGui.QPixmap("24861344486_b2a2f6805e_k.jpg")
		pixmap2 = pixmap.scaled(192, 108, PyQt4.QtCore.Qt.KeepAspectRatio)
		lbl2 = QtGui.QLabel(self)
		lbl2.setPixmap(pixmap2)

		hbox.addWidget(lbl2)
		self.setLayout(hbox)

		self.setFixedSize(320, 240)
		self.setWindowTitle("Reddit Wallpaper")
		self.show()


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


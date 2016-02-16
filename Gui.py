import sys
import RedditWallpaper
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot


def main():

	app = QtGui.QApplication(sys.argv)

	w = QtGui.QWidget()
	w.setFixedSize(320, 240)
	w.setWindowTitle('Reddit Wallpaper')

	@pyqtSlot()
	def on_press():
		RedditWallpaper.main("-db")

	btn = QtGui.QPushButton('Change background', w)
	btn.setToolTip('Change background')
	btn.clicked.connect(on_press)
	btn.resize(btn.sizeHint())
	btn.move(100, 80)

	w.show()

	exit(app.exec_())


if __name__ == '__main__':
	main()


import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtGui import QPixmap
import PyQt6.QtCore as QtCore
import PyQt6 as pq6
import seleniumbrowser
import myui
import time


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = myui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(540, 390)
        self.setWindowTitle("Mirea_Bot")
        self.ui.pushButton.clicked.connect(self.goto)
        pix = QPixmap()
        pix.load("pic.jpg")
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)
        r = scene.sceneRect()
        print(r)
        self.ui.graphicsView.fitInView(QtCore.QRectF(0,0,140,34))

    bot = seleniumbrowser.Bot()

    def goto(self):
        self.bot.goto(self.ui.input.text())
        while True:
            time.sleep(15)
            self.bot.check()



app = QApplication(sys.argv)
applic = MyApp()
applic.show()
sys.exit(app.exec())
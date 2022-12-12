import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigations
        navbar = QToolBar()
        self.addToolBar(navbar)

        back = QAction("<-", self)
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)

        forward_btn = QAction("->", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://wikipedia.com'))
    


app = QApplication(sys.argv)
QApplication.setApplicationName("Lilhar Browser")
window = MainWindow()
app.exec()

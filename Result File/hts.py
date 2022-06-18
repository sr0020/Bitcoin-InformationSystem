import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb
import pybithumb
import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from volatility import *

class VolatilityWorker(QThread):
    tradingSent = pyqtSignal(str, str, str)

    def __init__(self, ticker, bithumb):
        super().__init__()
        self.ticker = ticker
        self.bithumb = bithumb
        self.alive = True

    def close(self):
        self.alive = False

form_class = uic.loadUiType("resource/main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ticker = "BTC"
        self.setWindowTitle("Home Trading System")

        with open("bithumb.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)


    def receiveTradingSignal(self, time, type, amount):
        self.textEdit.append(f"[{time}] {type} : {amount}")

    def closeEvent(self, event):
        self.vw.close()
        self.widget.closeEvent(event)
        self.widget_2.closeEvent(event)
        self.widget_3.closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())

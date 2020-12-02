from PyQt5.QtWidgets import QMainWindow
import portSelectUI

class portSelectWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = portSelectUI.Ui_portSelect()
        self.ui.setupUi(self)

    def show_window(self):
        self.show()

    def hide_window(self):
        self.hide()
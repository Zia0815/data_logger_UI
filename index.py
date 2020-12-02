import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

# IMPORT UI WINDOW
import splash_window_UI
import port_select_window_UI

# info.py FILE CONTAINS VERSION AND PROJECT INFO
import info

print(f'name of project: {info.project} version: {info.app_version}')


class combinedWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash_window = splash_window_UI.splashWindow()
        self.port_select_window = port_select_window_UI.portSelectWindow()

        # TIMER FOR SPLASH SCREEN TIMEOUT
        self.timer_splash = QtCore.QTimer()
        self.timer_splash.timeout.connect(self.splash_window_progress)
        self.timer_splash.start(10)
        self.counter = 0

    # SPLASH SCREEN

    def show_splash_window(self):
        self.splash_window.show()

    def splash_window_progress(self):
        self.splash_window.ui.startProgressBar.setValue(self.counter)
        self.splash_window.ui.startProgressBar.setTextVisible(False)
        self.counter += 1
        if self.counter >= 100:
            self.initialize_port_select_window()
            self.splash_window.close()
            self.timer_splash.stop()

    def hide_splash_window(self):
        self.splash_window.hide()

    # PORT SELECTION SCREEN

    def initialize_port_select_window(self):
        self.port_select_window.show()

    def hide_splash_port_select_window(self):
        self.port_select_window.hide()

    def populate_port_list(self):
        self.port_select_window.ui.comboBox_port_sel.addItem("This")

    # ALL SCREEN INITIALIZATION

    def initialize_and_show(self):
        self.show_splash_window()
        self.populate_port_list()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    combined_window = combinedWindow()
    combined_window.initialize_and_show()
    sys.exit(app.exec_())

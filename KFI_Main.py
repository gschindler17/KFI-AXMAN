import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit
import KFI_GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KFI_GUI.MyApp()
    window.show()
    sys.exit(app.exec())
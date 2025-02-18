import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit
import KFI_Controller as Controller

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui", self)  # Load the UI file

        # Access the button by its object name from Qt Designer
        self.pushButton_1.clicked.connect(lambda: self.controller.handle_button_click(1))
        self.pushButton_2.clicked.connect(self.on_button_click2)
        self.pushButton_3.clicked.connect(self.on_button_click3)
        self.pushButton_4.clicked.connect(self.on_button_click4)
        self.pushButton_5.clicked.connect(self.on_button_click5)
        self.pushButton_6.clicked.connect(self.on_button_click6)
        self.pushButton_7.clicked.connect(self.on_button_click7)
        self.pushButton_8.clicked.connect(self.on_button_click8)
        self.pushButton_9.clicked.connect(self.on_button_click9)
        self.pushButton_10.clicked.connect(self.on_button_click10)
        self.pushButton_11.clicked.connect(self.on_button_click11)
        self.pushButton_12.clicked.connect(self.on_button_click12)
        self.pushButton_13.clicked.connect(self.on_button_click13)
        self.pushButton_14.clicked.connect(self.on_button_click14)
        self.pushButton_15.clicked.connect(self.on_button_click15)
        self.pushButton_16.clicked.connect(self.on_button_click16)
        self.pushButton_17.clicked.connect(self.on_button_click17)
        self.pushButton_18.clicked.connect(self.on_button_click18)
        self.pushButton_19.clicked.connect(self.on_button_click19)
        self.pushButton_20.clicked.connect(self.on_button_click20)
        self.pushButton_21.clicked.connect(self.on_button_click21)
        self.pushButton_22.clicked.connect(self.on_button_click22)
        self.pushButton_23.clicked.connect(self.on_button_click23)
        self.pushButton_24.clicked.connect(self.on_button_click24)

    def set_controller(self, controller):
        # Sets the controller instance after GUI initialization.
        print("KFI_GUI: Controller set.")
        self.controller = controller
    
    
    def on_button_click1(self):
        self.controller.handle_button_click(1)
        print("\nButton 1 clicked!")  # Action when button is clicked
        
    def on_button_click2(self):
        print("Button clicked!")  # Action when button is clicked    
    
    def on_button_click3(self):
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click4(self):
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click5(self):
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click6(self):
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click7(self):
        print("Button clicked!")  # Action when button is clicked

    def on_button_click8(self):
        print("Button clicked!")  # Action when button is clicked

    def on_button_click9(self):
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click10(self):
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click11(self):
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click12(self):
        print("Button clicked!")  # Action when button is clicked

    def on_button_click13(self):
        text = self.lineEdit.text()
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click14(self):
        text = self.lineEdit_2.text()
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click15(self):
        text = self.lineEdit_3.text()
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click16(self):
        text = self.lineEdit_4.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click17(self):
        text = self.lineEdit_5.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click18(self):
        text = self.lineEdit_6.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click19(self):
        text = self.lineEdit_7.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click20(self):
        text = self.lineEdit_8.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click21(self):
        text = self.lineEdit_9.text()
        print("Button clicked!")  # Action when button is clicked
        
    def on_button_click22(self):
        text = self.lineEdit_10.text()
        print("Button clicked!")  # Action when button is clicked
    
    def on_button_click23(self):
        text = self.lineEdit_11.text()
        print("Button clicked!")  # Action when button is clicked

    def on_button_click24(self):
        text = self.lineEdit_12.text()
        print("Button clicked!")  # Action when button is clicked



import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit
import KFI_Controller as Controller

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui", self)  # Load the UI file

        # Access the button by its object name from Qt Designer

        # self.pushButton_1.clicked.connect(lambda: self.controller.handle_button_click(1))
        # self.pushButton_2.clicked.connect(lambda: self.controller.handle_button_click(2))
        # self.pushButton_3.clicked.connect(lambda: self.controller.handle_button_click(3))
        # self.pushButton_4.clicked.connect(lambda: self.controller.handle_button_click(4))
        # self.pushButton_5.clicked.connect(lambda: self.controller.handle_button_click(5))
        # self.pushButton_6.clicked.connect(lambda: self.controller.handle_button_click(6))
        # self.pushButton_7.clicked.connect(lambda: self.controller.handle_button_click(7))
        # self.pushButton_8.clicked.connect(lambda: self.controller.handle_button_click(8))
        # self.pushButton_9.clicked.connect(lambda: self.controller.handle_button_click(9))
        # self.pushButton_10.clicked.connect(lambda: self.controller.handle_button_click(10))
        # self.pushButton_11.clicked.connect(lambda: self.controller.handle_button_click(11))
        # self.pushButton_12.clicked.connect(lambda: self.controller.handle_button_click(12))
        # self.pushButton_13.clicked.connect(self.on_button_click13)
        # self.pushButton_14.clicked.connect(self.on_button_click14)
        # self.pushButton_15.clicked.connect(self.on_button_click15)
        # self.pushButton_16.clicked.connect(self.on_button_click16)
        # self.pushButton_17.clicked.connect(self.on_button_click17)
        # self.pushButton_18.clicked.connect(self.on_button_click18)
        # self.pushButton_19.clicked.connect(self.on_button_click19)
        # self.pushButton_20.clicked.connect(self.on_button_click20)
        # self.pushButton_21.clicked.connect(self.on_button_click21)
        # self.pushButton_22.clicked.connect(self.on_button_click22)
        # self.pushButton_23.clicked.connect(self.on_button_click23)
        # self.pushButton_24.clicked.connect(self.on_button_click24)
        self.relay_1.clicked.connect(self.relay1_clicked)

    # Controller reference
    def set_controller(self, controller):
        # Sets the controller instance after GUI initialization.
        print("KFI_GUI: Controller set.")
        self.controller = controller
    
    # Controller reference
    # def on_button_click1(self):
    #     self.controller.handle_button_click(1)
    #     print("\nButton 1 clicked!")  # Action when button is clicked
    
    # GUI method
    def line_relay1_color(self, rgb_string):

        #TODO Change later
        rgb_string = "rgb(0, 255, 0)"

        self.line_relay1_1.setStyleSheet("background-color: {};".format(rgb_string))

        print("GUI: Relay 1 selected")
              
    
    # GUI method
    def line_relay2_color(self, rgb_string):

        #TODO Change later
        rgb_string = "rgb(0, 255, 0)"

        self.line_relay2_1.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay2_2.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay2_3.setStyleSheet("background-color: {};".format(rgb_string))

        print("GUI: Relay 2 selected")

        # GUI method
    def line_relay3_color(self, rgb_string):

        #TODO Change later
        rgb_string = "rgb(0, 255, 0)"

        self.line_relay3_1.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay3_2.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay3_3.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay3_4.setStyleSheet("background-color: {};".format(rgb_string))
        self.line_relay3_5.setStyleSheet("background-color: {};".format(rgb_string))

        print("GUI: Relay 3 selected")
   
    # GUI method
    def line_relay4_color(self, rgb_string):

        #TODO Change later
        rgb_string = "rgb(0, 255, 0)"

        self.line_relay4_1.setStyleSheet("background-color: {};".format(rgb_string))

        print("GUI: Relay 4 selected")


        
    # def on_button_click3(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click4(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click5(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click6(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click7(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked

    # def on_button_click8(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked

    # def on_button_click9(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click10(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click11(self):
    #     pass 
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click12(self):
    #     pass
    #     # print("Button clicked!")  # Action when button is clicked

    # def on_button_click13(self):
    #     pass
    #     text = self.lineEdit.text()
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click14(self):
    #     pass
    #     text = self.lineEdit_2.text()
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click15(self):
    #     pass
    #     text = self.lineEdit_3.text()
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click16(self):
    #     pass
    #     text = self.lineEdit_4.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click17(self):
    #     pass
    #     text = self.lineEdit_5.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click18(self):
    #     pass
    #     text = self.lineEdit_6.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click19(self):
    #     pass
    #     text = self.lineEdit_7.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click20(self):
    #     pass
    #     text = self.lineEdit_8.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click21(self):
    #     pass
    #     text = self.lineEdit_9.text()
    #     # print("Button clicked!")  # Action when button is clicked
        
    # def on_button_click22(self):
    #     pass
    #     text = self.lineEdit_10.text()
    #     # print("Button clicked!")  # Action when button is clicked
    
    # def on_button_click23(self):
    #     pass
    #     text = self.lineEdit_11.text()
    #     # print("Button clicked!")  # Action when button is clicked

    # def on_button_click24(self):
    #     pass
    #     text = self.lineEdit_12.text()
    #     # print("Button clicked!")  # Action when button is clicked



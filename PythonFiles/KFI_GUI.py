import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit
import PythonFiles.KFI_Controller as controller
import time

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui", self)  # Load the UI file

        # Access the button by its object name from Qt Designer
        self.relay_1.clicked.connect(lambda: self.controller.handle_relay_click(1))
        self.relay_1.setStyleSheet("border: 2px solid red;")
        self.relay_2.clicked.connect(lambda: self.controller.handle_relay_click(2))
        self.relay_2.setStyleSheet("border: 2px solid red;")
        self.relay_3.clicked.connect(lambda: self.controller.handle_relay_click(3))
        self.relay_3.setStyleSheet("border: 2px solid red;")
        self.volts_box_relay1.returnPressed.connect(lambda: self.controller.submit_volts(1, self.volts_box_relay1.text()))
        self.volts_box_relay2.returnPressed.connect(lambda: self.controller.submit_volts(2, self.volts_box_relay2.text()))
        self.volts_box_relay3.returnPressed.connect(lambda: self.controller.submit_volts(3, self.volts_box_relay3.text()))
        self.in_1.clicked.connect(lambda: self.toggle_voltage_read(1))
        self.in_2.clicked.connect(lambda: self.controller.toggle_output_pin(2))

    # Controller reference
    def set_controller(self, controller):
        # Sets the controller instance after GUI initialization.
        print("KFI_GUI: Controller set.")
        self.controller = controller
        self.toggle_voltage_read(1)
        
    # GUI method
    def line_relay_color(self, relay_id, rgb_string):
        
        if(relay_id == 1):
                self.line_relay1_1.setStyleSheet("background-color: {};".format(rgb_string))
                self.relay_1.setStyleSheet( "border: 2px solid {};".format(rgb_string) )
                print("GUI: Relay 1 selected")

        elif(relay_id == 2):
                self.line_relay2_1.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay2_2.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay2_3.setStyleSheet("background-color: {};".format(rgb_string))
                self.relay_2.setStyleSheet( "border: 2px solid {};".format(rgb_string) )
                print("GUI: Relay 2 selected")

        elif(relay_id == 3):
                self.line_relay3_1.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay3_2.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay3_3.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay3_4.setStyleSheet("background-color: {};".format(rgb_string))
                self.line_relay3_5.setStyleSheet("background-color: {};".format(rgb_string))
                self.relay_3.setStyleSheet( "border: 2px solid {};".format(rgb_string) )

                #TODO Update later (to fourth relay)
                self.line_relay4_1.setStyleSheet("background-color: {};".format(rgb_string))

                print("GUI: Relay 3 selected")

        elif(relay_id == 4):
                print("GUI: Relay 4 selected")


    def toggle_voltage_read(self, pin):
        print("KFI_GUI: Trying to toggle voltage read on pin ", pin)
        self.controller.toggle_voltage_read(1)
        # self.amps_box_relay3.setText("{}".format(voltage))

    def update_volts_boxes(self, volts_list):
        self.amps_box_relay1.setText("{}".format(volts_list[1]))
        self.amps_box_relay3.setText("{}".format(volts_list[3]))
            
        
    

            
    
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit
import PythonFiles.KFI_Controller as controller
import time

class KFI_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui", self)  # Load the UI file

        
        self.confirmButton.clicked.connect(self.update_line)
        
        # TODO Like this
        self.out_13.clicked.connect(lambda: self.controller.handle_out_click(0))
        self.out_13.setStyleSheet("border: 2px solid red;")
        self.out_14.clicked.connect(lambda: self.controller.handle_out_click(1))
        self.out_14.setStyleSheet("border: 2px solid red;")
        self.out_15.clicked.connect(lambda: self.controller.handle_out_click(2))
        self.out_15.setStyleSheet("border: 2px solid red;")
        self.out_16.clicked.connect(lambda: self.controller.handle_out_click(3))
        self.out_16.setStyleSheet("border: 2px solid red;")
        self.out_17.clicked.connect(lambda: self.controller.handle_out_click(4))
        self.out_17.setStyleSheet("border: 2px solid red;")
        self.out_18.clicked.connect(lambda: self.controller.handle_out_click(5))
        self.out_18.setStyleSheet("border: 2px solid red;")
        self.out_19.clicked.connect(lambda: self.controller.handle_out_click(6))
        self.out_19.setStyleSheet("border: 2px solid red;")
        self.out_20.clicked.connect(lambda: self.controller.handle_out_click(7))
        self.out_20.setStyleSheet("border: 2px solid red;")
        self.out_21.clicked.connect(lambda: self.controller.handle_out_click(8))
        self.out_21.setStyleSheet("border: 2px solid red;")
        self.out_22.clicked.connect(lambda: self.controller.handle_out_click(9))
        self.out_22.setStyleSheet("border: 2px solid red;")
        self.out_23.clicked.connect(lambda: self.controller.handle_out_click(10))
        self.out_23.setStyleSheet("border: 2px solid red;")
        self.out_24.clicked.connect(lambda: self.controller.handle_out_click(11))
        self.out_24.setStyleSheet("border: 2px solid red;")
        
        # self.in_1.clicked.connect(lambda:self.controller.handle_in_click(0))
        self.in_1.setStyleSheet("border: 2px solid red;")
        # self.in_2.clicked.connect(lambda:self.controller.handle_in_click(1))
        self.in_2.setStyleSheet("border: 2px solid red;")
        # self.in_3.clicked.connect(lambda:self.controller.handle_in_click(2))
        self.in_3.setStyleSheet("border: 2px solid red;")
        # self.in_4.clicked.connect(lambda:self.controller.handle_in_click(3))
        self.in_4.setStyleSheet("border: 2px solid red;")
        # self.in_5.clicked.connect(lambda:self.controller.handle_in_click(4))
        self.in_5.setStyleSheet("border: 2px solid red;")
        # self.in_6.clicked.connect(lambda:self.controller.handle_in_click(5))
        self.in_6.setStyleSheet("border: 2px solid red;")
        # self.in_7.clicked.connect(lambda:self.controller.handle_in_click(6))
        self.in_7.setStyleSheet("border: 2px solid red;")
        # self.in_8.clicked.connect(lambda:self.controller.handle_in_click(7))
        self.in_8.setStyleSheet("border: 2px solid red;")
        # self.in_9.clicked.connect(lambda:self.controller.handle_in_click(8))
        self.in_9.setStyleSheet("border: 2px solid red;")
        # self.in_10.clicked.connect(lambda:self.controller.handle_in_click(9))
        self.in_10.setStyleSheet("border: 2px solid red;")
        # self.in_11.clicked.connect(lambda:self.controller.handle_in_click(10))
        self.in_11.setStyleSheet("border: 2px solid red;")
        # self.in_12.clicked.connect(lambda:self.controller.handle_in_click(11))
        self.in_12.setStyleSheet("border: 2px solid red;")
        
        self.importButton.clicked.connect(self.import_text)
        
    # Controller reference
    def set_controller(self, controller):
        # Sets the controller instance after GUI initialization.
        print("KFI_GUI: Controller set.")
        self.controller = controller
        
    def update_line(self):
        
        self.controller.submit_bool_logic(self.boolInput.toPlainText())
            
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
    
    def out_button_color(self, button, rgb_string):
        if(button == 0):
            self.out_13.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 1):
            self.out_14.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 2):
            self.out_15.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 3):
            self.out_16.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 4):
            self.out_17.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 5):
            self.out_18.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 6):
            self.out_19.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 7):
            self.out_20.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 8):
            self.out_21.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 9):
            self.out_22.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 10):
            self.out_23.setStyleSheet("border: 2px solid {};".format(rgb_string))
        elif(button == 11):
            self.out_24.setStyleSheet("border: 2px solid {};".format(rgb_string))
    
    def update_inputs(self, inputpins):
        if inputpins[0] == 1:
            self.in_1.setStyleSheet('border: 2px solid green;')
        elif inputpins[0] != 1:
            self.in_1.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[1] == 1:
            self.in_2.setStyleSheet('border: 2px solid green;')
        elif inputpins[1] != 1:
            self.in_2.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[2] == 1:
            self.in_3.setStyleSheet('border: 2px solid green;')
        elif inputpins[2] != 1:
            self.in_3.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[3] == 1:
            self.in_4.setStyleSheet('border: 2px solid green;')
        elif inputpins[3] != 1:
            self.in_4.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[4] == 1:
            self.in_5.setStyleSheet('border: 2px solid green;')
        elif inputpins[4] != 1:
            self.in_5.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[5] == 1:
            self.in_6.setStyleSheet('border: 2px solid green;')
        elif inputpins[5] != 1:
            self.in_6.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[6] == 1:
            self.in_7.setStyleSheet('border: 2px solid green;')
        elif inputpins[6] != 1:
            self.in_7.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[7] == 1:
            self.in_8.setStyleSheet('border: 2px solid green;')
        elif inputpins[7] != 1:
            self.in_8.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[8] == 1:
            self.in_9.setStyleSheet('border: 2px solid green;')
        elif inputpins[8] != 1:
            self.in_9.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[9] == 1:
            self.in_10.setStyleSheet('border: 2px solid green;')
        elif inputpins[9] != 1:
            self.in_10.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[10] == 1:
            self.in_11.setStyleSheet('border: 2px solid green;')
        elif inputpins[10] != 1:
            self.in_11.setStyleSheet('border: 2px solid red;')
        time.sleep(.01)
        if inputpins[11] == 1:
            self.in_12.setStyleSheet('border: 2px solid green;')
        elif inputpins[11] != 1:
            self.in_12.setStyleSheet('border: 2px solid red;')
      
    def import_text(self): 
        filepath = self.textFileInput.text()
        print('getting filepath')
        try:
            print('opening filepath')
            with open(filepath, 'r', encoding='utf-8') as f:
                print('reading file')
                text = f.read()
                print('setting text')
                self.boolInput.setPlainText(text)
        except Exception as e:
                self.boolInput.setPlainText(f"Failed to read file:\n{str(e)}")        
            
    # def toggle_voltage_read(self, pin):
    #     print("KFI_GUI: Trying to toggle voltage read on pin ", pin)
    #     self.controller.toggle_voltage_read(1)
    #     # self.amps_box_relay3.setText("{}".format(voltage))

    # def update_volts_boxes(self, volts_list):
    #     self.amps_box_relay1.setText("{}".format(volts_list[1]))
    #     self.amps_box_relay3.setText("{}".format(volts_list[3]))
            

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QMessageBox
import PythonFiles.KFI_Controller as controller
import time

class KFI_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui", self)  # Load the UI file

        
        self.confirmButton.clicked.connect(self.update_line)
        self.confirmButton2.clicked.connect(self.update_line)
        
        # TODO Like this
        self.out_13.clicked.connect(lambda: self.controller.handle_out_click(0))
        self.out_13.setStyleSheet("border: 2px solid green;")
        self.out_14.clicked.connect(lambda: self.controller.handle_out_click(1))
        self.out_14.setStyleSheet("border: 2px solid green;")
        self.out_15.clicked.connect(lambda: self.controller.handle_out_click(2))
        self.out_15.setStyleSheet("border: 2px solid green;")
        self.out_16.clicked.connect(lambda: self.controller.handle_out_click(3))
        self.out_16.setStyleSheet("border: 2px solid green;")
        self.out_17.clicked.connect(lambda: self.controller.handle_out_click(4))
        self.out_17.setStyleSheet("border: 2px solid green;")
        self.out_18.clicked.connect(lambda: self.controller.handle_out_click(5))
        self.out_18.setStyleSheet("border: 2px solid green;")
        self.out_19.clicked.connect(lambda: self.controller.handle_out_click(6))
        self.out_19.setStyleSheet("border: 2px solid green;")
        self.out_20.clicked.connect(lambda: self.controller.handle_out_click(7))
        self.out_20.setStyleSheet("border: 2px solid green;")
        self.out_21.clicked.connect(lambda: self.controller.handle_out_click(8))
        self.out_21.setStyleSheet("border: 2px solid green;")
        self.out_22.clicked.connect(lambda: self.controller.handle_out_click(9))
        self.out_22.setStyleSheet("border: 2px solid green;")
        self.out_23.clicked.connect(lambda: self.controller.handle_out_click(10))
        self.out_23.setStyleSheet("border: 2px solid green;")
        self.out_24.clicked.connect(lambda: self.controller.handle_out_click(11))
        self.out_24.setStyleSheet("border: 2px solid green;")
        
        self.relay1.setStyleSheet('background-color: green;')
        self.relay2.setStyleSheet('background-color: green;')
        self.relay3.setStyleSheet('background-color: green;')
        
        # self.in_1.clicked.connect(lambda:self.controller.handle_in_click(0))
        self.in_1.setStyleSheet("border: 2px solid green;")
        # self.in_2.clicked.connect(lambda:self.controller.handle_in_click(1))
        self.in_2.setStyleSheet("border: 2px solid green;")
        # self.in_3.clicked.connect(lambda:self.controller.handle_in_click(2))
        self.in_3.setStyleSheet("border: 2px solid green;")
        # self.in_4.clicked.connect(lambda:self.controller.handle_in_click(3))
        self.in_4.setStyleSheet("border: 2px solid green;")
        # self.in_5.clicked.connect(lambda:self.controller.handle_in_click(4))
        self.in_5.setStyleSheet("border: 2px solid green;")
        # self.in_6.clicked.connect(lambda:self.controller.handle_in_click(5))
        self.in_6.setStyleSheet("border: 2px solid green;")
        # self.in_7.clicked.connect(lambda:self.controller.handle_in_click(6))
        self.in_7.setStyleSheet("border: 2px solid green;")
        # self.in_8.clicked.connect(lambda:self.controller.handle_in_click(7))
        self.in_8.setStyleSheet("border: 2px solid green;")
        # self.in_9.clicked.connect(lambda:self.controller.handle_in_click(8))
        self.in_9.setStyleSheet("border: 2px solid green;")
        # self.in_10.clicked.connect(lambda:self.controller.handle_in_click(9))
        self.in_10.setStyleSheet("border: 2px solid green;")
        # self.in_11.clicked.connect(lambda:self.controller.handle_in_click(10))
        self.in_11.setStyleSheet("border: 2px solid green;")
        # self.in_12.clicked.connect(lambda:self.controller.handle_in_click(11))
        self.in_12.setStyleSheet("border: 2px solid green;")
        
        self.importButton.clicked.connect(self.import_text)
        
        self.openRelay1.setText('7')
        self.closeRelay1.setText('8')
        self.statusRelay1.setText('22')
        self.openRelay2.setText('11')
        self.closeRelay2.setText('12')
        self.statusRelay2.setText('24')
        self.openRelay3.setText('9')
        self.closeRelay3.setText('10')
        self.statusRelay3.setText('23')

        self.textFileInput.setText('setting_configs/samplefile.txt')

        
        
        
    # Controller reference
    def set_controller(self, controller):
        # Sets the controller instance after GUI initialization.
        print("KFI_GUI: Controller set.")
        self.controller = controller



        
    def update_line(self):
        
        try:
            self.controller.submit_bool_logic(self.boolInput.toPlainText())
        except Exception as e:
            print(f"\n\nKFI_GUI: Exception[ERROR] Exception in submit_bool_logic: {e}\n\n")
        open_vals = [self.openRelay1.text(),self.openRelay2.text(), self.openRelay3.text()]
        close_vals =  [self.closeRelay1.text(),self.closeRelay2.text(), self.closeRelay3.text()]
        status_vals = [self.statusRelay1.text(), self.statusRelay2.text(), self.statusRelay3.text()]
        self.controller.pass_breaker_vals([1,2,3], open_vals, close_vals, status_vals )
        # self.controller.set_breaker_feedback([1,2,3],status_vals)

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
            time.sleep(.01)
        elif(button == 1):
            self.out_14.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 2):
            self.out_15.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 3):
            self.out_16.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 4):
            self.out_17.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 5):
            self.out_18.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 6):
            self.out_19.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 7):
            self.out_20.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 8):
            self.out_21.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 9):
            self.out_22.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 10):
            self.out_23.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
        elif(button == 11):
            self.out_24.setStyleSheet("border: 2px solid {};".format(rgb_string))
            time.sleep(.01)
    
    def update_inputs(self, inputpins):
        if inputpins[0] == 1:
            self.in_1.setStyleSheet('border: 2px solid red;')
        elif inputpins[0] != 1:
            self.in_1.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[1] == 1:
            self.in_2.setStyleSheet('border: 2px solid red;')
        elif inputpins[1] != 1:
            self.in_2.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[2] == 1:
            self.in_3.setStyleSheet('border: 2px solid red;')
        elif inputpins[2] != 1:
            self.in_3.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[3] == 1:
            self.in_4.setStyleSheet('border: 2px solid red;')
        elif inputpins[3] != 1:
            self.in_4.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[4] == 1:
            self.in_5.setStyleSheet('border: 2px solid red;')
        elif inputpins[4] != 1:
            self.in_5.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[5] == 1:
            self.in_6.setStyleSheet('border: 2px solid red;')
        elif inputpins[5] != 1:
            self.in_6.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[6] == 1:
            self.in_7.setStyleSheet('border: 2px solid red;')
        elif inputpins[6] != 1:
            self.in_7.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[7] == 1:
            self.in_8.setStyleSheet('border: 2px solid red;')
        elif inputpins[7] != 1:
            self.in_8.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[8] == 1:
            self.in_9.setStyleSheet('border: 2px solid red;')
        elif inputpins[8] != 1:
            self.in_9.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[9] == 1:
            self.in_10.setStyleSheet('border: 2px solid red;')
        elif inputpins[9] != 1:
            self.in_10.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[10] == 1:
            self.in_11.setStyleSheet('border: 2px solid red;')
        elif inputpins[10] != 1:
            self.in_11.setStyleSheet('border: 2px solid green;')
        time.sleep(.01)
        if inputpins[11] == 1:
            self.in_12.setStyleSheet('border: 2px solid red;')
        elif inputpins[11] != 1:
            self.in_12.setStyleSheet('border: 2px solid green;')
      
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
            
    def toggle_voltage_read(self, pin):
        print("KFI_GUI: Trying to toggle voltage read on pin ", pin)
        self.controller.toggle_voltage_read(1)
        # self.amps_box_relay3.setText("{}".format(voltage))  
       
    def update_breaker_feedback(self, breaker, feedback_vals):
        print("\n\ngui print:")
        print(feedback_vals)
        if feedback_vals[0]:
            self.relay1.setStyleSheet('background-color: red;')
        else:
            self.relay1.setStyleSheet('background-color: green;')
        if feedback_vals[1]:
            self.relay2.setStyleSheet('background-color: red;')
        else:
            self.relay2.setStyleSheet('background-color: green;')
        if feedback_vals[2]:
            self.relay3.setStyleSheet('background-color: red;')
        else:
            self.relay3.setStyleSheet('background-color: green;')         
              
    def arduino_crashed(self):
        QMessageBox.information('Error', 'Arduino Crashed. Restart GUI')
    # def update_volts_boxes(self, volts_list):
    #     self.amps_box_relay1.setText("{}".format(volts_list[1]))
    #     self.amps_box_relay3.setText("{}".format(volts_list[3]))
            

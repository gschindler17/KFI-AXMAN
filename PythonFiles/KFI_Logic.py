# TODO Fix the serial import on non-Rasp PI
import serial
import time
import threading
import re
import json
from PythonFiles.KFI_Arduino import KFI_Arduino

CONFIG_FILE = "config.json"

class KFI_Logic:
    def __init__(self):
        
        print("Logic Initialized")
        
        self.use_arduino = False
        self.arduino_object = None
        self.arduino_port = None
        self.get_config_data()

        

        # relay1_wire matches with first index, relay2_wire matches with second, etc.
        self.relay_wires = [False, False, False, False]

         # All initialized to off
        self.output_pin_states = [
            False, False, False, False, 
            False, False, False, False, 
            False, False, False, False
            ]
        
        self.input_pin_states = [
            False, False, False, False, 
            False, False, False, False, 
            False, False, False, False
            ]

    # Getting configuration data for the logic; only done on initialization
    def get_config_data(self):
        try:
            with open(CONFIG_FILE, "r") as file:
                config = json.load(file)
                self.use_arduino = config.get("use_arduino", False)  # Default to False if key is missing
                self.arduino_port = config.get("arduino_port", "/dev/ttyACM0")  # Default to False if key is missing
                
        except FileNotFoundError:
            print("Config file not found.")
            return False  # Default value if file is missing
    #---------------------------------------------------


    def process_button_action(self, button_id):
        print("Processed action for button {}".format(button_id))
        return f"Processed action for button {button_id}"  # Replace with actual logic

    def process_text_input(self, button_id, text):
        return text.upper()  # Example processing logic

    def process_relay_action(self, relay_id):
        print("Logic: Processed action for relay {}".format(relay_id))
        self.relay_wires[relay_id] = not self.relay_wires[relay_id]
        if (self.relay_wires[relay_id]):
            return "rgb(0, 255, 0)" 
        else:
            return "rgb(255, 0, 0)"
    
    def process_out_action(self, out_id):
        print("Logic: Processed action for relay {}".format(out_id))
        self.output_pin_states[out_id] = not self.output_pin_states[out_id]
        if (self.output_pin_states[out_id]):
            return "rgb(0, 255, 0)" 
        else:
            return "rgb(255, 0, 0)"    
    
    
    def get_pin_status(self, pinNum):
        return self.output_pin_states[pinNum]
    
    def set_output_pin(self, pin, pin_state):
        if (self.use_arduino):
            self.arduino_object.toggle_output_pin(pin, pin_state)
        else:
            print("KFI_Logic: setting pin:", self.output_pin_states[pin])
            print("\nKFI_Logic: No arduino in use, check config file.\n")
    
    def set_all_output_pins(self, pin_list):
        for i, val in enumerate(pin_list):
            self.set_output_pin(i, val)
    
    # Function to toggle pin on Arduino (abstracted by KFI_Arduino)
    def toggle_output_pin(self, pin):

        if (self.use_arduino):
            self.arduino_object.toggle_output_pin(pin, self.output_pin_states[pin])
        else:
            print("KFI_Logic: toggling pin:", self.output_pin_states[pin])
            print("\nKFI_Logic: No arduino in use, check config file.\n")

        if (self.output_pin_states[pin]):
            self.output_pin_states[pin] == False
        else:
            self.output_pin_states[pin] == True

        # print(self.output_pin_states)

    def setup_Arduino(self):
        if self.use_arduino == True:
            # Initialize the serial connection to Arduino (adjust the port as needed)
            self.arduino_object = KFI_Arduino(self.arduino_port, 9600)


    def READ_ALL_INPUTS(self):
        if (self.use_arduino):
            # print("Logic: READ_ALL_INPUTS")
            self.input_pin_states = self.arduino_object.READ_ALL_INPUTS()
            # print(f"KFI_Logic: input pins = {self.input_pin_states}")
        else:
            print("KFI_Logic: reading all inputs")
            print("\nKFI_Logic: No arduino in use, check config file.\n")

        return self.input_pin_states
        

    def evaluate_logic_code(self, code_str):
        inputs = self.input_pin_states
        outputs = self.output_pin_states

        new_outputs = outputs.copy()

        try:
            
            lines = [line.strip() for line in code_str.strip().split(';') if line.strip()]

            for line in lines:
                if '=' not in line:
                    continue

                lhs, rhs = line.split('=')
                output_index = int(lhs.strip()) - 13  # 13–24 maps to 0–11

                original_expression = rhs.strip()
                expression = original_expression

                # Replace T and F with True and False
                expression = re.sub(r'\bT\b', 'True', expression)
                expression = re.sub(r'\bF\b', 'False', expression)

                # Replace NOT (!) with Python's `not`
                expression = re.sub(r'!', 'not ', expression)

                # Replace logical operators: * → and, + → or
                expression = expression.replace('*', ' and ')
                expression = expression.replace('+', ' or ')

                # Replace pin numbers 1–24 with appropriate references
                def replace_pin_refs(match):
                    num = int(match.group())
                    if 1 <= num <= 12:
                        return f"inputs[{num - 1}]"
                    elif 13 <= num <= 24:
                        return f"new_outputs[{num - 13}]"
                    return match.group()

                expression = re.sub(r'\b([1-9]|1[0-9]|2[0-4])\b', replace_pin_refs, expression)

                try:
                    result = bool(eval(expression, {'inputs': inputs, 'new_outputs': new_outputs}))
                    new_outputs[output_index] = result

                except Exception as e:
                    print(f"[ERROR] Failed to evaluate line '{line}': {e}")

            self.output_pin_states = new_outputs

        except Exception as e:
            print("\n\nKFI_Logic: INVALID BOOLEAN COMMAND FOUND\n\n")
            raise e

        return new_outputs 

    def get_breaker_feedback(self, breaker, feedback):
        feedback_vals = []
        for i, val in enumerate(feedback):
            feedback_vals.append(self.output_pin_states[int(feedback[i]) - 13])
        print("Logic: feedback_vals:", feedback_vals)
        if len(feedback_vals) < 1:
            feedback_vals = [False, False, False]
        return feedback_vals


    def get_arduino_crashed(self):
        return self.arduino_object.get_arduino_crashed()

# Example usage (adjust port as needed)
if __name__ == "__main__":
    print("Running KFI_Logic.py")
    logic = KFI_Logic.KFILogic()
    

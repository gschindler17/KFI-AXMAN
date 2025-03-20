import serial
import time


class KFI_Arduino:
    def __init__(self, comm_type, port_num):
        
        # All initialized to off
        self.pin_states = [
            False, False, False, False, 
            False, False, False, False, 
            False, False, False, False
            ]
        
        self.arduino = serial.Serial(comm_type, port_num)
        time.sleep(1)

    #Function to toggle pin and update label
    def toggle_pin(self, pin):
        self.arduino.write(bytes([pin]))  # Send the pin index to Arduino (0-3)
        print(f"KFI_Arduino: Toggling pin {pin}")

        # Check the current state of the pin and update label
        if self.pin_states[pin]:
            self.pin_states[pin] = False
        else:
            self.pin_states[pin] = True

    def set_pin_states(self, new_pin_states):
        self.pin_states = new_pin_states

    def get_pin_states(self):
        return self.pin_states
           
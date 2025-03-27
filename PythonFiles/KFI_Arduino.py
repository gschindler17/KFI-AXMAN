import serial
import time


class KFI_Arduino:
    def __init__(self, comm_type, port_num):
        
        # Creates a serial link to the Arduino
        # How commands are sent
        self.arduino = serial.Serial(comm_type, port_num)
        time.sleep(0.05)

    #Function to toggle pin and update label
    def toggle_output_pin(self, pin, bool_state):
        self.arduino.write(bytes([pin, int(bool_state)]))
        print(f"KFI_Arduino: Toggling pin {pin}")

        # Wait for a response from Arduino
        response = self.arduino.readline().decode().strip()
        if response:
            print(f"Arduino Response: {response}")
        else:
            print("No response from Arduino.")


    

           
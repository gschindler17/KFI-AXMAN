import serial
import time
import threading


class KFI_Arduino:
    def __init__(self, comm_type, port_num):
        
        # Creates a serial link to the Arduino
        # How commands are sent
        self.pin_nums = [20,19,18,17,16,15,14,13,12,11,10,9]
        self.input_pin_nums = [52,50,48,46,44,42,40,38,36,34,32,28]
        self.arduino = serial.Serial(comm_type, port_num, timeout=1)
        
        self.thread_lock = threading.Lock() #Prevents simultaneous writes
        
        
        time.sleep(0.05)


    #Function to toggle pin and update label
    def toggle_output_pin(self, pin, bool_state):
        with self.thread_lock:
            if self.pin_nums[pin] not in self.pin_nums or bool_state not in [True, False]:
                print("Invalid pin or state")
                print("\nPin: ", pin, " State:", bool_state, "\n")
                return
            
            state_set = "LOW"
            if bool_state:
                state_set = "HIGH"

            message = f"{self.pin_nums[pin]},{state_set}\n"
            print(f"Sent: {message.strip()}")
            response = None

            
            self.arduino.write(message.encode())  # Send data to Arduino
            response = self.arduino.readline().decode().strip()
            
            # Read response from Arduino
            if response:
                print(f"Arduino Response: {response}")
        pass
        
    
    # SHOULD RETURN AN ARRAY OF BOOLEANS
    def READ_ALL_INPUTS(self):
        
        with self.thread_lock:
            
            message = "READ\n"
            message.strip()
            response = None
            self.arduino.write(message.encode())  # 0xA0: Custom command to request a pin reading
            response = self.arduino.readline().decode().strip()
            
            if response:
                print(f"KFI_Arduino: Completed read all inputs: _{response.strip()}_")

            return_list = [0,0,0,0,0,0,0,0,0,0,0,0]
            try:
                return_list = list(map(int, response.split(',')))
            except:
                print("KFI_Arduino: Unformattable input from the Arduino")

            return return_list



    
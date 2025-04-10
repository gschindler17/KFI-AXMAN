import serial
import time
import threading


class KFI_Arduino:
    def __init__(self, comm_type, port_num):
        
        # Creates a serial link to the Arduino
        # How commands are sent
        self.pin_nums = [33,32,31,30,29,28,27,26,25,24,23,22]
        self.input_pin_nums = [53,52,51,50,49,48,47,46,45,44,43,42,41]
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



    
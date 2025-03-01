# TODO Fix the serial import on non-Rasp PI
import serial
import time
import threading
import json

CONFIG_FILE = "config.json"

class KFILogic:
    def __init__(self):
        
        print("Logic Initialized")
        
        self.use_arduino = False
        self.get_config_data()

        # relay1_wire matches with first index, relay2_wire matches with second, etc.
        self.relay_wires = [False, False, False, False]

        # Stores voltages for each relay (relay 1 matches index 1)
        self.relay_volts = ["0", "0", "0", "0"]

        # Toggles for whether or not voltages should be read
        self.voltage_toggles = [False, False, False, False]

        # List of all threads active or inactive
        self.thread1 = threading.Thread(target= lambda: self.read_voltage(1), daemon=True )
        self.thread2 = None

    def get_config_data(self):
        try:
            with open(CONFIG_FILE, "r") as file:
                config = json.load(file)
                self.use_arduino = config.get("use_arduino", False)  # Default to False if key is missing
        except FileNotFoundError:
            print("Config file not found.")
            return False  # Default value if file is missing

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

    def submit_volts(self, relay_id, text):
        self.relay_volts[relay_id] = text
        print(f"Logic: New relay {relay_id} value {text} volts")

    def toggle_voltage_read(self, voltage_num):
        if (self.voltage_toggles[voltage_num] == True):
            self.voltage_toggles[voltage_num] = False
            print("KFI_Logic: Toggled {} voltage reader to off".format(voltage_num))
        else:
            self.voltage_toggles[voltage_num] = True
            self.thread1 = threading.Thread(target= lambda: self.read_voltage(voltage_num), daemon=True )
            self.thread1.start()
            print("KFI_Logic: Toggled on {} voltage reader".format(voltage_num))
    
    def read_voltage(self, pin, port='/dev/ttyACM0', baudrate=9600, interval=0.2):
        if (self.use_arduino):
            try:
                while (self.voltage_toggles[pin]):
                    with serial.Serial(port, baudrate, timeout=0.5) as ser:
                        time.sleep(1)  # Allow time for serial connection to initialize
                        if ser.in_waiting > 0:
                            voltage = ser.readline().decode().strip()
                            print(f"Voltage: {voltage} V for pin {pin}")

                            time.sleep(interval)
                            return voltage

            except serial.SerialException as e:
                print(f"Error: {e}")
                return 999
        
        else:
            # TODO Use a config file
            # Version for PC Only
            count = 0
            while (self.voltage_toggles[pin]):
                time.sleep(2)
                # print("KFI_Logic: Pin {} sleeping...".format(pin))
                count = count + 1
                self.relay_volts[pin] = count
                print("KFI_Logic: self.relay_volts = ", count)
                pass

    def get_relay_volts(self):
        return self.relay_volts

        
    

# Example usage (adjust port as needed)
if __name__ == "__main__":
    print("Running KFI_Logic.py")
    logic = KFILogic()
    logic.read_voltage('/dev/ttyACM0')  # Change this based on the correct port


        


    

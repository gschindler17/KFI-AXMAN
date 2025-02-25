import serial
import time

class KFILogic:
    def __init__(self):
        print("Logic Initialized")

        # relay1_wire matches with first index, relay2_wire matches with second, etc.
        self.relay_wires = [False, False, False, True]

        # Stores voltages for each relay (relay 1 matches index 1)
        self.relay_volts = ["0", "0", "0", "0"]


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


    def read_voltage(self, pin, port='/dev/ttyUSB0', baudrate=9600, interval=0.2):
        try:
            with serial.Serial(port, baudrate, timeout=0.5) as ser:
                time.sleep(2)  # Allow time for serial connection to initialize
                if ser.in_waiting > 0:
                    voltage = ser.readline().decode().strip()
                    print(f"Voltage: {voltage} V for pin {pin}")

                    time.sleep(interval)
                    return voltage

        except serial.SerialException as e:
            print(f"Error: {e}")
            return 999

# Example usage (adjust port as needed)
if __name__ == "__main__":
    print("Running KFI_Logic.py")
    logic = KFILogic()
    logic.read_voltage('/dev/ttyACM0')  # Change this based on the correct port


        


    

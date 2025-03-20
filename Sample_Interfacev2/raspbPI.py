import tkinter as tk
import serial
import time

# Initialize the serial connection to Arduino (adjust the port as needed)
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Adjust for your Raspberry Pi's Arduino port
time.sleep(2)  # Wait for Arduino to initialize

# Function to toggle pin
def toggle_pin(pin):
    arduino.write(bytes([pin]))  # Send the pin index to Arduino (0-3)
    print(f"Button {pin} clicked, toggling pin {pin}")

# Create the main window
root = tk.Tk()
root.title("Arduino Pin Toggle")

# Create four buttons for the pins
buttons = []
for i in range(4):
    button = tk.Button(root, text=f"Toggle Pin {i+1}", command=lambda i=i: toggle_pin(i))
    button.pack(pady=10)
    buttons.append(button)

# Start the GUI loop
root.mainloop()

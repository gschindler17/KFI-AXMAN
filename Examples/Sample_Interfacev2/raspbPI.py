import tkinter as tk
import serial
import time

# Initialize the serial connection to Arduino (adjust the port as needed)
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Adjust for your Raspberry Pi's Arduino port
time.sleep(2)  # Wait for Arduino to initialize

# Function to toggle pin and update label
def toggle_pin(pin, label):
    arduino.write(bytes([pin]))  # Send the pin index to Arduino (0-3)
    print(f"Button {pin} clicked, toggling pin {pin}")

    # Check the current state of the pin and update label
    if pin_states[pin]:
        pin_states[pin] = False
        label.config(text=f"Pin {pin+1} is OFF", bg='red')
    else:
        pin_states[pin] = True
        label.config(text=f"Pin {pin+1} is ON", bg='green')

# Initial states of the pins (all OFF initially)
pin_states = [False, False, False, False]

# Create the main window
root = tk.Tk()
root.title("Arduino Pin Toggle")

# Create a list to hold buttons and labels
buttons = []
labels = []

# Create 4 buttons and 4 labels for the pins
for i in range(4):
    button = tk.Button(root, text=f"Toggle Pin {i+1}", command=lambda i=i: toggle_pin(i, labels[i]))
    button.pack(pady=10)
    
    label = tk.Label(root, text=f"Pin {i+1} is OFF", width=20, height=2, bg='red')
    label.pack(pady=5)
    
    buttons.append(button)
    labels.append(label)

# Start the GUI loop
root.mainloop()

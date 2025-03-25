import serial
import time

# Open serial connection (adjust the port if necessary)
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)  # Allow time for the connection to initialize

# Send a message
arduino.write(b"Hello Arduino\n")

# Read response
response = arduino.readline().decode().strip()
print("Arduino says:", response)

arduino.close()

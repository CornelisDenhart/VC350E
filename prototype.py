#!/usr/bin/python3

# https://pyserial.readthedocs.io/en/latest/shortintro.html

import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=1200, timeout=5)  # open serial port
print(ser.name)         # check which port was really used

ser.write(bytes.fromhex('c90d'))     # Reset, seems not to work
time.sleep(1)
s = ser.readline()
print (s)

ser.write(bytes.fromhex('cb') + bytes.fromhex('0d'))     # Power off disable, not working
time.sleep(1)
s = ser.readline()
print (s)

ser.write(bytes.fromhex('f00d'))     # Check function, working
time.sleep(1)
s = ser.readline()
print (s)

ser.write(bytes.fromhex('f10d'))     # Check range, working
time.sleep(1)
s = ser.readline()
print (s)

ser.write(bytes.fromhex('E00d'))     # Measure value read, working
time.sleep(1)
s = ser.readline()
print (s)

ser.close()


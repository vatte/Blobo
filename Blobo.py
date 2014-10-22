#!/usr/bin/env python
#Blobo.py

"""
This is a simple python2.7 driver for Blobo.
Run with serial port as argument to test:
e.g. $ python Blobo.py /dev/rfcomm0

#usage with this file in your folder:
from Blobo import Blobo
blobo = Blobo(<serial port>, <data handling function>)

#to exit:
blobo.alive = False

Requires pySerial.

Copyright Valtteri Wikstrom
Licensed under the MIT License
"""

import serial
import time
import struct
from threading import Thread

class Blobo:
	def __init__(self, device, updatefunc):
		self.update = updatefunc
		self.ser = serial.Serial(device)
		self.data = []
		#data format: 4 bytes, 10 2-byte integers, 1 byte
		self.key = 'BBBBhhhhhhhhhhB'
		time.sleep(5)

		self.t = time.time()
		self.ser.write(chr(65))

		self.alive = True # thread will shutdown when alive is set to False
		self.readThread = Thread(target=self.read)
		self.readThread.start()

	def read(self):
		while(self.alive):
			line = struct.unpack(self.key, self.ser.read(25))
			if line[0] == 0 and line[1] == 65:
				#we're interested in the integers
				self.data = line[4:-1]
				self.update(self.data)
			if time.time()-self.t > 1:
				#keeping connection alive
				self.t = time.time()
				self.ser.write(chr(13))




if __name__ == "__main__":
	import sys
	global blobo

	def print_data(data):
		print ("accelerometer :\t" + '\t'.join(str(w) for w in data[0:3]))
		print ("gyroscope :\t" + '\t'.join(str(w) for w in data[3:6]))
		print ("magnetometer :\t" + '\t'.join(str(w) for w in data[6:9]))
		print ("pressure :\t" + str(data[9]))


	if len(sys.argv) < 2:
		raise Exception("No serial device provided as argument!")
	else:
		blobo = Blobo(sys.argv[1], print_data)

	#keep main thread alive and wait for CTRL-C for exit
	try:
		while True:
			time.sleep(5)
	except KeyboardInterrupt:
		blobo.alive = False

#run with argument /dev/rfcomm0 or /dev/rfcomm1

import serial
import time
import struct
import sys

if len(sys.argv) < 2:
	exit('1st argument: serial port name')

#ser = serial.Serial(91, 115200)
#ser = serial.Serial('/dev/rfcomm0', 115200)
ser = serial.Serial(sys.argv[1])
#key = 'BBBBBBBBBBBBBBBBBBBBBBBBB'
key = 'BBBBhhhhhhhhhhB'

while True:
	time.sleep(5)
	if ser.isOpen():
		break

t = time.time()

ser.write(chr(65))

while(1):
	line = struct.unpack(key, ser.read(25))
	if line[0] == 0 and line[1] == 65:
		print('\t'.join(map(str, line[4:-1])))
	if time.time()-t > 1:
		#keeping connection alive
		t = time.time()
		ser.write(chr(13))

		
	


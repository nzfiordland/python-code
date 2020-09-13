#-------------------------------------------------------------------------------
# Name:		module1
# Purpose:
#
# Author:	  o'neilld
#
# Created:	 05/03/2012
# Copyright:   (c) o'neilld 2012
# Licence:	 <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import serial
from time import sleep

port = "\\\\.\\COM1"
ser = serial.Serial(port, 4800, timeout=None)
#ser = serial.Serial(0)

count = 0
text = ''

# read from serial port & return (print to screen) read data
def serialRead():
    data = ser.read(100)
    if len(data) > 0:
        print (data)
    return

#ser.write("at\n".encode())

while serialRead() != '\n':
      #sleep(2)
      serialRead()

##    sleep(0.5)
##    print 'not blocked'

ser.close()


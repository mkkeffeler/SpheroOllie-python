#!/usr/bin/python
import struct
import time
import Ollie_driver
import sys
ollie = Ollie_driver.Sphero()
ollie.connect()


ollie.start()
time.sleep(2)
ollie.set_rgb_led(255,0,0,0,False)
time.sleep(1)
ollie.set_rgb_led(0,255,0,0,False)
time.sleep(1)
ollie.set_rgb_led(0,0,255,0,False)
time.sleep(3)
ollie.set_stablization(False,'False')
while 1:
	key = raw_input("what is your character")
	if(key == "l"):
		ollie.set_raw_motor_values(1,60,1,40,'01h')
	if(key== "j"):
		ollie.set_raw_motor_values(1,40,1,60,'01h')
	if(key== "i"):
		ollie.set_raw_motor_values(1,60,1,60,'01h')
	if(key == "k"):
		ollie.set_raw_motor_values(2,60,2,60,'01h')
	if(key=='g'):
		break
time.sleep(5)
ollie.join()
sys.exit(1)


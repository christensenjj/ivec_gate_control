## @file gpio_ref.py
# @brief GPIO Reference
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file contains methods that provide GPIO setup and access operations.

import RPi.GPIO as GPIO
import time
from threading import Thread

## @brief Class to manage the simple interactions with the GPIO pins
## Operations that involve generating or reading complex signals are left to the specific drivers
class GPIORef:
	## Initialization function for the GPIO Ref Class
	def __init__(self):
		## Current IP Address
		self.ip_address = "127.0.0.1"
		## Boolean stating if the state is normally open
		self.normal_open = True
		## Boolean stating if the digital input has been triggered
		self.di_trigger = False
		## Reference time for the last DI trigger
		self.di_trigger_time = 0
		## Boolean stating whether to flash the motion LED or not
		self.motion = False
		## Thread to manage the LED Flashing
		self.motion_thread = 0
		## Boolean to keep LED thread alive
		self.active = True

	NO_NC_SW = 7
	LED_ERROR = 11
	LED_MOT	= 13
	LED_CLOSED = 15
	LED_INT = 19
	LED_OPEN = 21
	M_FAULT = 27
	M_HIGH = 29
	M_LOW = 31
	ALERT2 = 8
	ALERT1 = 10
	DIGIN = 12
	IPADDR7 = 16
	IPADDR6 = 18
	IPADDR5 = 22
	IPADDR4 = 24
	IPADDR3 = 26
	IPADDR2 = 28
	IPADDR1 = 36
	IPADDR0 = 38

	## Callback for the digital input switch
        def di_callback(self):
		self.di_trigger = True if (GPIO.input(self.DIGIN) == GPIO.LOW) else False
		if not self.di_trigger :
			self.di_trigger_time = time.time() * 1000
		print "DI Triggered"

	## Callback for the normally open/closed toggle switch
	def nonc_callback(self):
		self.normal_open = True if (GPIO.input(self.NO_NC_SW) == GPIO.LOW) else False
		print ("Normal Open: ", self.normal_open)


	## A function to flash the motion LED based on a global variable in a separate thread
	def in_motion(self, flash, active):
		while active() :
			if flash() :
				GPIO.output(self.LED_MOT, GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(self.LED_MOT, GPIO.HIGH)
				time.sleep(0.5)
				print "Flashing"


	## A function for setting all of the GPIO pins to their necessary states.
	def setup_gpio(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		# Outputs
		GPIO.setup(self.LED_ERROR, GPIO.OUT)
		GPIO.setup(self.LED_MOT, GPIO.OUT)
		GPIO.setup(self.LED_CLOSED, GPIO.OUT)
		GPIO.setup(self.LED_INT, GPIO.OUT)
		GPIO.setup(self.LED_OPEN, GPIO.OUT)
		# Inputs
		GPIO.setup(self.IPADDR0, GPIO.IN)
		GPIO.setup(self.IPADDR1, GPIO.IN)
		# GPIO.setup(self.IPADDR2, GPIO.IN)
		GPIO.setup(self.IPADDR3, GPIO.IN)
		GPIO.setup(self.IPADDR4, GPIO.IN)
		GPIO.setup(self.IPADDR5, GPIO.IN)
		GPIO.setup(self.IPADDR6, GPIO.IN)
		GPIO.setup(self.IPADDR7, GPIO.IN)
		GPIO.setup(self.DIGIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.NO_NC_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.DIGIN, GPIO.BOTH, callback=self.di_callback)
		GPIO.add_event_detect(self.NO_NC_SW, GPIO.BOTH, callback=self.nonc_callback)
		self.motion_thread = Thread(target = self.in_motion, args=(lambda : self.motion, lambda : self.active, ))
		self.active = True
		self.motion_thread.start()

	## A function for retrieving the current IP address, read from the external DIP switch
	def get_ip_address(self):
		host_number = 0
		host_number |= ((1 if GPIO.input(self.IPADDR7) == GPIO.HIGH else 0) << 7)
		host_number |= ((1 if GPIO.input(self.IPADDR6) == GPIO.HIGH else 0) << 6)
		host_number |= ((1 if GPIO.input(self.IPADDR5) == GPIO.HIGH else 0) << 5)
		host_number |= ((1 if GPIO.input(self.IPADDR4) == GPIO.HIGH else 0) << 4)
		host_number |= ((1 if GPIO.input(self.IPADDR3) == GPIO.HIGH else 0) << 3)
		host_number |= ((1 if GPIO.input(self.IPADDR2) == GPIO.HIGH else 0) << 2)
		host_number |= ((1 if GPIO.input(self.IPADDR1) == GPIO.HIGH else 0) << 1)
		host_number |= ((1 if GPIO.input(self.IPADDR0) == GPIO.HIGH else 0) << 0)
		self.ip_address = "127.0.0." + str(host_number)
		print ("IP Address: ", self.ip_address)
		return self.ip_address


	## A function for setting the status of the LEDs
	#
	# @param motion: A boolean value that indicates whether or not the gate is in motion
	# @param position: An integer in the range 0-100 indicating the position of the gate.
	# @param error: A boolean value that indicates if an error has occurred or if service is needed
	def set_led_out(self, motion, position, error):
		self.motion = motion
		if(position == 0):
			GPIO.output(self.LED_OPEN, GPIO.HIGH)
			GPIO.output(self.LED_CLOSED, GPIO.LOW)
			GPIO.output(self.LED_INT, GPIO.LOW)
		elif(position < 100):
			GPIO.output(self.LED_OPEN, GPIO.LOW)
			GPIO.output(self.LED_CLOSED, GPIO.LOW)
			GPIO.output(self.LED_INT, GPIO.HIGH)
		else:
			GPIO.output(self.LED_OPEN, GPIO.LOW)
			GPIO.output(self.LED_CLOSED, GPIO.HIGH)
			GPIO.output(self.LED_INT, GPIO.LOW)

		if error :
			GPIO.output(self.LED_ERR, GPIO.HIGH)
		else:
			GPIO.

	## A function to get the status of the digital input(s) and indicate whether any of them remain active.
	#
	# @return A boolean value that indicates if a digital input is still active
	def get_di_states(self):
		self.di_trigger = True if (GPIO.input(self.DIGIN) == GPIO.LOW) else False
		return self.di_trigger

	## Method to cleanup the GPIO assignments
	def gpio_cleanup(self):
		GPIO.cleanup()
		self.active = False
		self.motion_thread.join()

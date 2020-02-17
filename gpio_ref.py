## @file gpio_ref.py
# @brief GPIO Reference
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file contains methods that provide GPIO setup and access operations.

import RPi.GPIO as GPIO

## @brief Class to manage the simple interactions with the GPIO pins
## Operations that involve generating or reading complex signals are left to the specific drivers
class GPIORef:
	## Initialization function for the GPIO Ref Class
	def __init__(self):
		## Current IP Address
		self.ip_address = "127.0.0.1"
		## Boolean stating if the state is normally open
		self.normal_open = False
		## Boolean stating if the digital input has been triggered

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
		self.di_trigger = True
		print "DI Triggered"

	## Callback for the normally open/closed toggle switch
	def nonc_callback(self):
		self.normal_open ^= True
		print ("Normal Open: ", self.normal_open)

	## A function for setting all of the GPIO pins to their necessary states.
	def setup_gpio(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		inputs = [7, 8, 10, 16, 18, 22, 24, 26, 28, 36, 38]
		GPIO.setup(inputs, GPIO.IN)
		GPIO.setup(DIGIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(DIGIN, GPIO.FALLING, callback=di_callback)
		GPIO.add_event_detect(NO_NC_SW, GPIO.BOTH, callback=nonc_callback)

	## A function for retrieving the current IP address, read from the external DIP switch
	def get_ip_address(self):
		host_number = 0
		host_number |= ((1 if GPIO.input(IPADDR7) == GPIO.HIGH else 0) << 7)
		host_number |= ((1 if GPIO.input(IPADDR6) == GPIO.HIGH else 0) << 6)
		host_number |= ((1 if GPIO.input(IPADDR5) == GPIO.HIGH else 0) << 5)
		host_number |= ((1 if GPIO.input(IPADDR4) == GPIO.HIGH else 0) << 4)
		host_number |= ((1 if GPIO.input(IPADDR3) == GPIO.HIGH else 0) << 3)
		host_number |= ((1 if GPIO.input(IPADDR2) == GPIO.HIGH else 0) << 2)
		host_number |= ((1 if GPIO.input(IPADDR1) == GPIO.HIGH else 0) << 1)
		host_number |= ((1 if GPIO.input(IPADDR0) == GPIO.HIGH else 0) << 0)
		self.ip_address = "127.0.0." + str(host_number)
		print ("IP Address: ", self.ip_address)
		return self.ip_address

	## A function for setting the status of the LEDs
	#
	# @param motion: A boolean value that indicates whether or not the gate is in motion
	# @param position: An integer in the range 0-100 indicating the position of the gate.
	# @param error: A boolean value that indicates if an error has occurred or if service is needed
	def set_led_out(self, motion, position, error):
		print("TODO: set_led_out")

	## A function to get the status of the digital input(s) and indicate whether any of them remain active.
	#
	# @return A boolean value that indicates if a digital input is still active
	def get_di_states(self):
		return (True if (GPIO.input(DIGIN) == GPIO.LOW else False)




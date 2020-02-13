## @file gpio_ref.py
# @brief GPIO Reference
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file contains methods that provide GPIO setup and access operations.

import RPi.GPIO as GPIO

class GPIORef:
	## Initialization function for the GPIO Ref Class
	def __init__(self):
		self.ip_address = "127.0.0.1"
		self.normal_open = False

	## Pin names and numbers
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

	## A function for setting all of the GPIO pins to their necessary states.
	def setup_gpio(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		inputs = [7, 8, 10, 12, 16, 18, 22, 24, 26, 28, 36, 38]
		GPIO.setup(inputs, GPIO.IN)

	## A function for retrieving the current IP address, read from the external DIP switch
	def get_ip_address(self):
		print("TODO: get_ip_address")
		return self.ip_address

	## A function for setting the status of the LEDs
	#
	# @param motion: A boolean value that indicates whether or not the gate is in motion
	# @param position: An integer in the range 0-100 indicating the position of the gate.
	# @param error: A boolean value that indicates if an error has occured or if service is needed
	def set_led_out(self, motion, position, error):
		print("TODO: set_led_out")

	## A function to get the status of the digital input(s) and indicate whether any of them remain active.
	#
	# @return A boolean value that indicates if a digital input is still active
	def get_di_states(self):
		print("TODO: get_di_states")




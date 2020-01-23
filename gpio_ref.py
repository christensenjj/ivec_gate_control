"""
Title: GPIO Reference
File: gpio_ref.py
Author: Jacob Christensen <christensenjj@msoe.edu>
Date: 01/22/2020
Description:
	This file contains methods that provide GPIO setup and access operations.
"""
import RPi.GPIO as GPIO




"""
A function for setting all of the GPIO pins to their necessary states.
:returns: NONE
"""
def setup_gpio():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

"""
A function for retrieving the current IP address, read from the external DIP switch

:returns: A value in the range of 0-255
"""
def get_ip_address():


"""
A function for setting the status of the LEDs

:param motion: A boolean value that indicates whether or not the gate is in motion
:param position: An integer in the range 0-100 indicating the position of the gate.
:param error: A boolean value that indicates if an error has occured or if service
	      is needed
:returns: NONE
"""
def set_led_out(motion, position, error):



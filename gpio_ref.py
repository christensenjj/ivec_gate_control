## @file gpio_ref.py
# @brief GPIO Reference
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file contains methods that provide GPIO setup and access operations.

import RPi.GPIO as GPIO




## A function for setting all of the GPIO pins to their necessary states.
def setup_gpio():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)


## A function for retrieving the current IP address, read from the external DIP switch
def get_ip_address():



## A function for setting the status of the LEDs
#
# @param motion: A boolean value that indicates whether or not the gate is in motion
# @param position: An integer in the range 0-100 indicating the position of the gate.
# @param error: A boolean value that indicates if an error has occured or if service is needed
def set_led_out(motion, position, error):


## A function to get the status of the digital input(s) and indicate whether any of them remain active.
#
# @return A boolean value that indicates if a digital input is still active
def get_di_states():




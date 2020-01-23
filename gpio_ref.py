"""
Title: GPIO Reference
File: gpio_ref.py
Author: Jacob Christensen <christensenjj@msoe.edu>
Date: 01/22/2020
Description:
	This file contains methods that provide GPIO setup and access operations.
"""
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def setup_gpio():
	


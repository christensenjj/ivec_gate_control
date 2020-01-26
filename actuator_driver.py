"""
Title: Actuator Driver
File: actuator_driver.py
Author: Jacob Christensen <christensenjj@msoe.edu>
Date: 01/22/2020
Description:
	This file will contain the functions required to create the appropriate signal
	to drive the linear actuator through the motor controller.
"""

import data_collection as DC

"""
This function will move the actuator to the set position

:params position: Number (0-100) to indicate percentage open
:returns: NONE
"""
def set_postion(position):


"""
This function will set the duty cycle for the PWM signal for the motor controller

:params duty_cycle: Number (0-100) to indicate duty cycle for PWM signal
:returns: NONE
"""
def set_position(duty_cycle):


"""
This function will start the actuator moving forwards (according to motor controller)

:returns: NONE
"""
def start_fwd():


"""
This function will start the actuator moving backwards (according to motor controller)

:returns: NONE
"""
def start_bwd():


"""
This function will disable the motor controller, stopping the actuator

:returns: NONE
"""
def stop_actuator():



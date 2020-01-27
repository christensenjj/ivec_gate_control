## @file actuator_driver.py
# Title: Actuator Driver
# Author: Jacob Christensen <christensenjj@msoe.edu>
# Date: 01/22/2020
# Description:
# 	This file will contain the functions required to create the appropriate signal
#	to drive the linear actuator through the motor controller.


import data_collection as DC


##This function will move the actuator to the set position
#
# @param position Number (0-100) to indicate percentage open
def set_postion(position):



##This function will set the duty cycle for the PWM signal for the motor controller
#
# @param duty_cycle Number (0-100) to indicate duty cycle for PWM signal
def set_position(duty_cycle):


##This function will start the actuator moving forwards (according to motor controller)
def start_fwd():


##This function will start the actuator moving backwards (according to motor controller)
def start_bwd():


##This function will disable the motor controller, stopping the actuator
def stop_actuator():



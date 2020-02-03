## @file actuator_driver.py
# @brief Actuator Driver
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file will contain the functions required to create the appropriate signal to drive the linear actuator through the motor controller.

import data_collection as DC
import RPi.GPIO as GPIO

class ActuatorDriver:

	# Maximum current allowed before "Safe-Stop" is triggered
	max_current = 150
	# Pin for output of pwm signal for moving forward
	pwm_fwd = 33
	# Pin for output of PWM signal for moving in reverse
	pwm_rev = 32

	## This fucntion initializes the Actuator Driver object
	#
	# @param duty_cycle The starting duty_cycle of the PWM signal
	def __init__(self, duty_cycle) :
		self.duty_cycle = duty_cycle
		self.fwd_out = GPIO.PWM(pwm_fwd, 1000)
		self.rev_out = GPIO.PWM(pwm_rev, 1000)

	##This function will move the actuator to the set position
	#
	# @param position Number (0-100) to indicate percentage open
	def set_position(self, position) :
		current_pos = DC.get_position()
		current_draw = DC.get_current()
		# If the gate is open, start the actuator moving forward to close
		if(position > current_pos):
			self.start_fwd()
			while (position > current_pos) and (self.max_current > current_draw) :
				current_pos = DC.get_position()
				current_draw = DC.get_current()
		# If the gate is closed, start the actuator moving in reverse to open
		elif(position < current_pos):
			self.start_bwd()
			while(position < current_pos) and (self.max_current > current_draw) :
				current_pos = DC.get_position()
				current_draw = DC.get_current()
		# Stop the actuator if the position is reached or the current draw is too high
		self.stop_actuator()

	## This function will set the duty cycle for the PWM signal for the motor controller
	#
	# @param duty_cycle Number (0-100) to indicate duty cycle for PWM signal
	def set_pwm(self, duty_cycle) :
		self.duty_cycle = duty_cycle
		self.fwd_out.ChangeDutyCycle(duty_cycle)
		self.rev_out.ChangeDutyCycle(duty_cycle)

	## This function will start the actuator moving forwards (according to motor controller)
	def start_fwd(self):
		self.rev_out.stop()
		self.fwd_out.start(self.duty_cycle)

	## This function will start the actuator moving backwards (according to motor controller)
	def start_bwd(self):
		self.fwd_out.stop()
		self.rev_out.start(self.duty_cycle)

	## This function will disable the motor controller, stopping the actuator
	def stop_actuator(self):
		self.fwd_out.stop()
		self.rev_out.stop()




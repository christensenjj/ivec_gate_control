## @file actuator_driver.py
# @brief Actuator Driver
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file will contain the functions required to create the appropriate signal to drive the linear actuator through the motor controller.

import data_collection as DC

class ActuatorDriver:

	# Maximum current allowed before "Safe-Stop" is triggered
	max_current = 150

	## This fucntion initializes the Actuator Driver object
	#
	# @param duty_cycle The starting duty_cycle of the PWM signal
	def __init__(self, duty_cycle) :
		self.duty_cycle = duty_cycle

	##This function will move the actuator to the set position
	#
	# @param position Number (0-100) to indicate percentage open
	def set_position(self, position) :
		current_pos = DC.get_position()
		current_draw = DC.get_current()
		if(position > current_pos):
			self.start_fwd()
			while (position > current_pos) and (self.max_current > current_draw) :
				current_pos = DC.get_position()
				current_draw = DC.get_current()
			self.stop_actuator()

	## This function will set the duty cycle for the PWM signal for the motor controller
	#
	# @param duty_cycle Number (0-100) to indicate duty cycle for PWM signal
	def set_pwm(self, duty_cycle) :
		self.duty_cycle = duty_cycle
		print(self.duty_cycle)

	## This function will start the actuator moving forwards (according to motor controller)
	def start_fwd(self):
		print("TODO: start_fwd")

	## This function will start the actuator moving backwards (according to motor controller)
	def start_bwd(self):
		print("TODO: start_bwd")

	## This function will disable the motor controller, stopping the actuator
	def stop_actuator(self):
		print("TODO: stop_actuator")




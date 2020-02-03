## @file actuator_driver.py
# @brief Actuator Driver
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file will contain the functions required to create the appropriate signal to drive the linear actuator through the motor controller.

from gpio_ref import GPIORef
import data_collection as DC
import RPi.GPIO as GPIO

## @brief Class to manage signal generation for actuator motion
class ActuatorDriver:

	## This fucntion initializes the Actuator Driver object
	#
	# @param duty_cycle The starting duty_cycle of the PWM signal
	# @param gr Instance of GPIORef for LED functions
	def __init__(self, duty_cycle, gr) :
		self.gr = gr
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pwm_fwd, GPIO.OUT)
		GPIO.setup(self.pwm_rev, GPIO.OUT)
		self.duty_cycle = duty_cycle
		self.fwd_out = GPIO.PWM(self.pwm_fwd, 1000)
		self.rev_out = GPIO.PWM(self.pwm_rev, 1000)

	## Maximum current allowed before "Safe-Stop" is triggered
	max_current = 150
	## Pin for output of pwm signal for moving forward
	pwm_fwd = 33
	## Pin for output of PWM signal for moving in reverse
	pwm_rev = 32

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
				self.gr.set_led_out(True, current_pos, False)
		# If the gate is closed, start the actuator moving in reverse to open
		elif(position < current_pos):
			self.start_bwd()
			while(position < current_pos) and (self.max_current > current_draw) :
				current_pos = DC.get_position()
				current_draw = DC.get_current()
				self.gr.set_led_out(True, current_pos, False)
		# Stop the actuator if the position is reached or the current draw is too high
		self.stop_actuator()
		self.gr.set_led_out(False, current_pos, None)

	## This function will set the duty cycle for the PWM signal for the motor controller
	#
	# @param duty_cycle Number (0-100) to indicate duty cycle for PWM signal
	def set_pwm(self, duty_cycle) :
		self.duty_cycle = duty_cycle
		self.fwd_out.ChangeDutyCycle(duty_cycle)
		self.rev_out.ChangeDutyCycle(duty_cycle)

	## Start the actuator motion
	#
	# Motion will be in the "closing" direction
	def start_fwd(self):
		self.rev_out.stop()
		self.fwd_out.start(self.duty_cycle)

	## Start the actuator motion
	#
	# Motion will be in the "opening" direction
	def start_bwd(self):
		self.fwd_out.stop()
		self.rev_out.start(self.duty_cycle)

	## Stop the actuator motion
	#
	# Halt the generation of the PWM signals
	def stop_actuator(self):
		self.fwd_out.stop()
		self.rev_out.stop()




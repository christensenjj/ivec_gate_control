## @file actuator_driver.py
# @brief Actuator Driver
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/22/2020
# @details This file will contain the functions required to create the appropriate signal to drive the linear actuator through the motor controller.

import RPi.GPIO as GPIO
from data_collection import DataCollection

## @brief Class to manage signal generation for actuator motion
class ActuatorDriver:

    ## This function initializes the Actuator Driver object
    #
    # @param duty_cycle The starting duty_cycle of the PWM signal
    # @param gr Instance of GPIORef for access to GPIO functions
    # @param dc Instance of DataCollection for access to sensor data
    def __init__(self, duty_cycle, gr, dc):
        ## Instance of GPIORef for access to GPIO functions
        self.gr = gr
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pwm_fwd, GPIO.OUT)
        GPIO.setup(self.pwm_rev, GPIO.OUT)
        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.output(self.relay_pin, GPIO.LOW)
        ## Instance of DataCollection for access to sensor data
        self.dc = dc
        ## The duty cycle of the PWM signal driving the actuator
        self.duty_cycle = duty_cycle
        ## PWM instance for forward motion
        self.fwd_out = GPIO.PWM(self.pwm_fwd, 1000)
        ## PWM instance for reverse motion
        self.rev_out = GPIO.PWM(self.pwm_rev, 1000)

    ## Maximum current allowed before "Safe-Stop" is triggered
    max_current = 150
    ## Pin for output of pwm signal for moving forward
    pwm_fwd = 33
    ## Pin for output of PWM signal for moving in reverse
    pwm_rev = 32
    ## Pin to trigger electro-mechanical relay
    relay_pin = 23

    ##This function will move the actuator to the set position
    #
    # @param position Number (0-100) to indicate percentage open
    def set_position(self, position):
        current_pos = self.dc.get_position()
        current_draw = self.dc.get_current()
        # If the gate is open, start the actuator moving forward to close
        if(position > current_pos):
            self.start_fwd()
            while (position > current_pos) and (self.max_current > current_draw) :
                current_pos = self.dc.get_position()
                current_draw = self.dc.get_current()
                self.gr.set_led_out(True, current_pos, False)
        # If the gate is closed, start the actuator moving in reverse to open
        elif(position < current_pos):
            self.start_bwd()
            while(position < current_pos) and (self.max_current > current_draw) :
                current_pos = self.dc.get_position()
                current_draw = self.dc.get_current()
                self.gr.set_led_out(True, current_pos, False)
        # Stop the actuator if the position is reached or the current draw is too high
        self.stop_actuator()
        event = "Safe-Stop - Current Overdraw Detected" if (current_draw > self.max_current) else "Position Reached"
        self.dc.write_data_log("Event: %s | Position: %d | Current Draw: %d " % (event, current_pos, current_draw))
        self.gr.set_led_out(False, current_pos, (current_draw > self.max_current))

    ## This function will set the duty cycle for the PWM signal for the motor controller
    #
    # @param duty_cycle Number (0-100) to indicate duty cycle for PWM signal
    def set_pwm(self, duty_cycle):
        self.duty_cycle = duty_cycle
        self.fwd_out.ChangeDutyCycle(duty_cycle)
        self.rev_out.ChangeDutyCycle(duty_cycle)

    ## Start the actuator motion
    #
    # Motion will be in the "closing" direction
    def start_fwd(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
        self.rev_out.stop()
        self.fwd_out.start(self.duty_cycle)

    ## Start the actuator motion
    #
    # Motion will be in the "opening" direction
    def start_bwd(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
        self.fwd_out.stop()
        self.rev_out.start(self.duty_cycle)

    ## Stop the actuator motion
    #
    # Halt the generation of the PWM signals
    def stop_actuator(self):
        GPIO.output(self.relay_pin, GPIO.LOW)
        self.fwd_out.stop()
        self.rev_out.stop()




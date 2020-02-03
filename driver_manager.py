## @file driver_manager.py
# @brief Driver Manager
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/20/2020
# @details This driver manager will act as the entry point for the entire software control system. This file will control access to system hardware through the rest of the drivers. This file will also setup interrupt service routines for real-time response to activation


from actuator_driver import ActuatorDriver
from gpio_ref import GPIORef

##Callback for edge event on Normally Open/Closed Switch"
def ncno_callback():
	print("TODO: ncno_callback")

## Callback for edge event on digital input 1
def di_callback():
	print("TODO: di_callback")


## Main execution for control system software
def main():
	gpio.setup_gpio()
	actuator.set_pwm(70)
	actuator.set_position(40)

if __name__ == "__main__":
	# Instantiate the GPIO reference object
	gpio = GPIORef()
	# Instantiate ActuatorDriver with 60% duty cycle
	actuator = ActuatorDriver(60, gpio)
	# Run top level code
	main()


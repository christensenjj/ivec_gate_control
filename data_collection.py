## @file data_collection.py
# @brief Data Collection
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/26/2020
# @details This file will hold much of the functionality required for gathering and processing data from the peripherals of the microcontroller. This file will also pieces of the data collected back to the memory for future access.



##This function will setup the appropriate pins for communication with the Analog-to-Digital converter.
def adc_setup():
	print("TODO: adc_setup")

##This function will read the current from the Hall Effect sensor
# @returns: A number representing the current being drawn by the actuator
def get_current():
	print("TODO: get_current")
	return 0

##This function will get the position of the actuator by reading the potentiometer value from the ADC.
# @returns A number representing the position of the actuator
def get_position():
	print("TODO: get_position")
	return 0

##This function will write out given information to a log file for future access
# @param info Information to be written
def write_data_log(info):
	print("TODO: write_data_log(info)")



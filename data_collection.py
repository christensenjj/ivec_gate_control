## @file data_collection.py
# @brief Data Collection
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/26/2020
# @details This file will hold much of the functionality required for gathering and processing data from the peripherals of the microcontroller. This file will also pieces of the data collected back to the memory for future access.

import logging

## This class is used to manage interactions withe ADC and sensors
class DataCollection:
	## Function to setup the DataCollection object
	def __init__(self):
		## Data logger for tracking data gathered from sensors
		self.logger = logging.getLogger()
		handler = logging.FileHandler('dataLog.log')
		formatter = logging.Formatter('%(asctime)s %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		self.logger.setLevel(logging.INFO)

	##This function will setup the appropriate pins for communication with the Analog-to-Digital converter.
	def adc_setup(self):
		print("TODO: adc_setup")

	##This function will read the current from the Hall Effect sensor
	# @returns: A number representing the current being drawn by the actuator
	def get_current(self):
		print("TODO: get_current")
		return 160

	##This function will get the position of the actuator by reading the potentiometer value from the ADC.
	# @returns A number representing the position of the actuator
	def get_position(self):
		print("TODO: get_position")
		return 0

	##This function will write out given information to a log file for future access
	# @param info Information string to be written to log file
	def write_data_log(self, info):
		self.logger.info(info)



## @file data_collection.py
# @brief Data Collection
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/26/2020
# @details This file will hold much of the functionality required for gathering and processing data from the peripherals of the microcontroller. This file will also pieces of the data collected back to the memory for future access.

import logging

import Adafruit_ADS1x15

## This class is used to manage interactions with the ADCs and sensors
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
		## ADC objects for reading information from the sensors
		self.adc1 = Adafruit_ADS1x15.ADS1115()
		self.adc2 = Adafruit_ADS1x15.ADS1115(address=0x49)

	## Gain to be used when reading from the sensors
	GAIN = 1
	## Current sensor channel
	CURRENT = 1
	## Postion sensor channel
	POSITION = 2


	##This function will read the current from the Hall Effect sensor
	# @returns: A number representing the current being drawn by the actuator
	def get_current(self):
		current = 0
		# current = self.adc1.read_adc(CURRENT, gain=GAIN)
		return current

	##This function will get the position of the actuator by reading the potentiometer value from the ADC.
	# @returns A number representing the position of the actuator
	def get_position(self):
		position = 0
		# POSITION = self.adc1.read_adc(POSITION, gain=GAIN)
		return position

	##This function will write out given information to a log file for future access
	# @param info Information string to be written to log file
	def write_data_log(self, info):
		self.logger.info(info)




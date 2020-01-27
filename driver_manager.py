## @file driver_manager.py
# Title: Driver Manager
# Author: Jacob Christensen <christensenjj@msoe.edu>
# Date: 01/20/2020
# Description:
#     This driver manager will act as the entry point for the entire software
#     control system. This file will control access to system hardware through
#     the rest of the drivers. This file will also setup interrupt service
#     routines for real-time response to activation."

import actuator_driver
import gpio_ref


##Callback for edge event on Normally Open/Closed Switch"
def ncno_callback():



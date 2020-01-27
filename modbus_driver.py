
## @file modbus_driver.py
# Title: Modbus Driver
# Author: Jacob Christensen <christensenjj@msoe.edu>
# Date: 01/26/2020
# Description:
# 	This file will setup a TCP Modbus Server that monitors and responds to changes in the
# 	Modbus memory structure.


from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import (ModbusRtuFramer,
                                  ModbusAsciiFramer,
                                  ModbusBinaryFramer)
from custom_message import CustomModbusRequest

## Function to configure and start the Modbus Server.
def run_async_server():

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17]*100),
        co=ModbusSequentialDataBlock(0, [17]*100),
        hr=ModbusSequentialDataBlock(0, [17]*100),
        ir=ModbusSequentialDataBlock(0, [17]*100))
    store.register(CustomModbusRequest.function_code, 'cm',
                   ModbusSequentialDataBlock(0, [17] * 100))
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '2.3.0'

    ## Start TCP Server
    StartTcpServer(context, identity=identity, address=("localhost", 5020),
                   custom_functions=[CustomModbusRequest])



##This function will read the Modbus Memory Context to check for updates
#
# @param ctxt Memory Context to read
# @returns Values read from memory context
def read_context(ctxt):



## This function will write out to the Modbus Memory Context
#
# @param ctxt Memory context to write to
# @params values Values to write out
def write_update(ctxt, values):




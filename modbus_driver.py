## @file modbus_driver.py
# @brief Modbus Driver
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/26/2020
# @details This file will setup a TCP Modbus Server that monitors and responds to changes in the Modbus memory structure.


from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import (ModbusRtuFramer,
                                  ModbusAsciiFramer,
                                  ModbusBinaryFramer)

## @brief Class to manage the setup and access for the TCP based Modbus Server
class ModbusDriver:
    ## Initializes the ModbusDriver Class
    def __init__(self):
        store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [17]*100),
            co=ModbusSequentialDataBlock(0, [17]*100),
            hr=ModbusSequentialDataBlock(0, [17]*100),
            ir=ModbusSequentialDataBlock(0, [17]*100))
        ## Reference to the server context for reading from and writing to
        self.context = ModbusServerContext(slaves=store, single=True)

    ## Function to configure and start the Modbus Server.
    def run_async_server(self):
        identity = ModbusDeviceIdentification()
        identity.VendorName = 'Pymodbus'
        identity.ProductCode = 'PM'
        identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
        identity.ProductName = 'Pymodbus Server'
        identity.ModelName = 'Pymodbus Server'
        identity.MajorMinorRevision = '2.3.0'
        ## Start TCP Server
        StartTcpServer(self.context, identity=identity, address=("localhost", 5020))

    ##This function will read the Modbus Memory Context to check for updates
    #
    # @param ctxt Memory Context to read
    # @returns Values read from memory context
    def read_context(self, ctxt):
        context  = ctxt[0]
        register = 3
        slave_id = 0x00
        address  = 0x00
        value = context[slave_id].getValues(register,address)[0]
        print value
        return value


    ## This function will write out to the Modbus Memory Context
    #
    # @param ctxt Memory context to write to
    # @param values Values to write out
    def write_update(self, ctxt):
        context  = ctxt[0]
        value = [ctxt[1]]
        register = 3
        slave_id = 0x00
        address  = 0x00
        if(value != self.read_context(ctxt)):
            context[slave_id].setValues(register,address,value)




## @file driver_manager.py
# @brief Driver Manager
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/20/2020
# @details This driver manager will act as the entry point for the entire software control system. This file will control access to system hardware through the rest of the drivers. This file will also setup interrupt service routines for real-time response to activation


from twisted.internet.task import LoopingCall
from actuator_driver import ActuatorDriver
from gpio_ref import GPIORef
from data_collection import DataCollection
from modbus_driver import ModbusDriver


## Callback for edge event on Normally Open/Closed Switch"
def ncno_callback():
    # Changes the Normally Open/Closed setting
    print "TODO: ncno_callback"

## Callback for edge event on digital input 1
def di_callback():
    # Used to trigger the gate sequence from digital input 1
    print "TODO: di_callback"


## Main execution for control system software
def main():
    # Setup functions
    GPIO.setup_gpio()
    DC.adc_setup()
    loop = LoopingCall(MODBUS.read_context, ctxt=(MODBUS.context,))
    loop2 = LoopingCall(MODBUS.write_update, ctxt=(MODBUS.context,25,))
    ACTUATOR.set_pwm(70)
    ACTUATOR.set_position(40)
    loop.start(2)
    loop2.start(5)
    MODBUS.run_async_server()

if __name__ == "__main__":
    # Instantiate the GPIO reference object
    GPIO = GPIORef()
    # Instantiate the Data Collection object
    DC = DataCollection()
    # Instantiate the Modbus Driver Object
    MODBUS = ModbusDriver()
    # Instantiate ActuatorDriver with 60% duty cycle
    ACTUATOR = ActuatorDriver(60, GPIO, DC)
    # Run top level code
    main()

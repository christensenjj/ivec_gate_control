## @file driver_manager.py
# @brief Driver Manager
# @author Jacob Christensen <christensenjj@msoe.edu>
# @date 01/20/2020
# @details This driver manager will act as the entry point for the entire software control system. This file will control access to system hardware through the rest of the drivers. This file will also setup interrupt service routines for real-time response to activation


from twisted.internet.task import LoopingCall, deferLater
from twisted.internet import reactor
from actuator_driver import ActuatorDriver
from gpio_ref import GPIORef
from data_collection import DataCollection
from modbus_driver import ModbusDriver
import time

## Open/Close the gate based on digital input or MODBUS command
def gate_action():
    print "Loop Call"
    if(not GPIO.motion):
        print "Loop not in Motion"
        if(GPIO.get_di_states()) :
            if(GPIO.normal_open) :
                ACTUATOR.set_position(0)
            else :
                ACTUATOR.set_position(100)
        elif(((time.time() * 1000) - GPIO.di_trigger_time) < 15000) :
            ACTUATOR.set_position(100)
        else :
            ACTUATOR.set_position(MODBUS.read_context((MODBUS.context,)))

## Main execution for control system software
def main():
    # Setup functions
    GPIO.setup_gpio()
    ACTUATOR.set_pwm(70)
    ACTUATOR.set_position(40)
    loop = LoopingCall(gate_action)
    # init_position = deferLater(reactor, 0.25, MODBUS.write_update, (MODBUS.context, 0))
    loop.start(0.25)
    # reactor.run()
    MODBUS.run_async_server()
    GPIO.gpio_cleanup()

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

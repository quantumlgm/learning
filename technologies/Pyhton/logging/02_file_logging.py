"""
Lesson 2: Configuration, File Logging, and Severity Overrides

Short Description:
Configuring the root logger to redirect all severity levels to an external log file.

Detailed Description:
This module demonstrates the dynamic runtime modification of the Python logging engine:
- Overrides the default WARNING threshold to capture granular DEBUG and INFO execution steps.
- Configures 'logging.basicConfig' to target a dedicated physical file system resource.
- Enforces a clear session state policy by utilizing filemode='w' to truncate old logs on startup.
"""

import logging

logging.basicConfig(level=logging.DEBUG, filename="02_coffee_machine.log", filemode="w")


class CoffeeMachine:
    def activation(self):
        logging.info("Coffee machine is starting up")

    def scan(self):
        logging.debug("Checking the details...")

    def cups_emptied(self):
        logging.warning("We're running out of cups")

    def machine_error(self):
        logging.error("Payment error on Bank side")

    def machine_bolt(self):
        logging.critical("The coffee machine is broken!")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    coffee_machine.activation()
    coffee_machine.scan()
    coffee_machine.cups_emptied()
    coffee_machine.machine_bolt()

    """ 
    After running the code, we'll see a new file containing the following entry:
    
    INFO:root:Coffee machine is starting up
    DEBUG:root:Checking the details...
    WARNING:root:We're running out of cups
    CRITICAL:root:The coffee machine is broken!
    """

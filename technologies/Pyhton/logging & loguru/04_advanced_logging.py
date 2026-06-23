"""
Lesson 4: Advanced Logging Architecture - Loggers, Handlers, and Formatters

Short Description:
Decoupling log logic from the root logger by constructing a manual OOP routing engine.

Detailed Description:
This module demonstrates corporate-grade logging infrastructure pipeline design:
- Instantiates an isolated, named 'Logger' instance detached from Python's global root state.
- Orchestrates multi-destination log routing using independent 'StreamHandler' and 'FileHandler' objects.
- Binds unique 'Formatter' layouts and discrete severity thresholds to distinct target outputs.
"""

import logging

logger = logging.getLogger("coffee_service")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s -> %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("04_system.log", "w")
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] (%(funcName)s) -> %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


class CoffeeMachine:
    def activation(self):
        logger.info("Coffee machine is starting up")

    def scan(self):
        logger.debug("Checking the details...")

    def cups_emptied(self):
        logger.warning("We're running out of cups")

    def machine_error(self):
        logger.error("Payment error on Bank side")

    def machine_bolt(self):
        logger.critical("The coffee machine is broken!")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    coffee_machine.activation()  # INFO -> Coffee machine is starting up
    coffee_machine.scan()  # This isn't being logged because the DEBUG level is ignored by the console handler.
    coffee_machine.cups_emptied()  # WARNING -> We're running out of cups
    coffee_machine.machine_bolt()  
    """
    in console: CRITICAL -> The coffee machine is broken!

    in file: [2026-06-23 18:18:36,982] [CRITICAL] (machine_bolt) -> The coffee machine is broken!
    """ 


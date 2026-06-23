"""
Lesson 1: Python Logging Basics and Default Behaviors

Short Description:
Exploring the standard logging library, its built-in severity levels, and default filtering thresholds.

Detailed Description:
This module demonstrates the application of logging severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL):
- Simulates real-world application events using a stateful class representation.
- Illustrates Python's default behavior, which suppresses DEBUG and INFO messages.
- Verifies that only logs meeting or exceeding the default WARNING threshold are output to sys.stderr.
"""

import logging


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

    """
    This is not logged because the logging configuration has default 
    settings that do not log messages below the WARNING level.
    """
    coffee_machine.activation()
    coffee_machine.scan()

    coffee_machine.cups_emptied()  # WARNING:root:We're running out of cups
    coffee_machine.machine_bolt()  # CRITICAL:root:The coffee machine is broken!

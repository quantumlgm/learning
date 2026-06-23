"""
Lesson 6: Introduction to Loguru, Sinks, and JSON Serialization

Short Description:
Migrating from standard logging to Loguru's simplified, single-logger streaming architecture.

Detailed Description:
This module demonstrates the structural paradigms of the Loguru library:
- Eliminates standard OOP boilerplate by utilizing a single unified global 'logger' control unit.
- Configures multi-destination routing using the universal 'logger.add' sink management system.
- Validates the generation of production-ready structured logging via JSON serialization lines.
"""

from loguru import logger
from sys import stdout

logger.remove()
logger.add(stdout, format="{time:HH:mm:ss} -> {message}", level="INFO")

logger.add("06_loguru.log", level="WARNING", serialize=True)


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

    coffee_machine.activation()
    coffee_machine.scan()
    coffee_machine.cups_emptied()
    coffee_machine.machine_bolt()

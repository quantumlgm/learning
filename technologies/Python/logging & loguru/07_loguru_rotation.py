"""
Lesson 7: Loguru Management - Log Rotation and Retention Policies

Short Description:
Implementing automated file truncation and cleanup rules using high-level Loguru sinks.

Detailed Description:
This module demonstrates automatic handling of log file lifetimes under constrained environment conditions:
- Configures dynamic size-based file splitting ('rotation') without utilizing 'TimedRotatingFileHandler'.
- Implements strict file system cleanup rules ('retention') to bound total log directory disk usage.
- Simulates heavy production environments using high-frequency loop generation to verify routing triggers.
"""

from loguru import logger

logger.remove()

logger.add("07_loguru.log", rotation="10 KB", retention=2)


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
    for count in range(200):
        coffee_machine.activation()
        coffee_machine.scan()
        coffee_machine.cups_emptied()
        coffee_machine.machine_bolt()

    """ 
    First, check the directory.
    There are 3 files inside where logs are written.
    """

"""
Lesson 5: Custom Logger Factories and Dependency Injection

Short Description:
Encapsulating logging configuration into factory functions and injecting logger dependencies into classes.

Detailed Description:
This module demonstrates the final architectural refactoring of the Python logging pipeline:
- Implements a Factory Pattern ('get_logger') to abstract the boilerplate setup of handlers and formatters.
- Enables scalable multi-instance logging by removing hardcoded module-level global logger states.
- Prepares the codebase for clean dependency injection, allowing classes to receive tailored Logger instances via '__init__'.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(levelname)s -> %(message)s")
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler("05_system.log", "w")
    file_handler.setLevel(logging.ERROR)
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] (%(funcName)s) -> %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = get_logger("coffee_logger")


class CoffeeMachine:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def activation(self):
        self.logger.info("Coffee machine is starting up")

    def scan(self):
        self.logger.debug("Checking the details...")

    def cups_emptied(self):
        self.logger.warning("We're running out of cups")

    def machine_error(self):
        self.logger.error("Payment error on Bank side")

    def machine_bolt(self):
        self.logger.critical("The coffee machine is broken!")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(logger)

    coffee_machine.activation()  # INFO -> Coffee machine is starting up
    coffee_machine.scan()  # This isn't being logged because the DEBUG level is ignored by the console handler.
    coffee_machine.cups_emptied()  # WARNING -> We're running out of cups
    coffee_machine.machine_bolt()
    """
    in console: CRITICAL -> The coffee machine is broken!

    in file: [2026-06-23 18:18:36,982] [CRITICAL] (machine_bolt) -> The coffee machine is broken!
    """

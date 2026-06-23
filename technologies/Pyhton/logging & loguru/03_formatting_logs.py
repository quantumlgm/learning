"""
Lesson 3: Advanced Log Formatting and LogRecord Attributes

Short Description:
Customizing log message layouts using legacy percent-style string formatting and system metadata.

Detailed Description:
This module demonstrates runtime layout configuration via Pydantic... structural formatting:
- Utilizes standard 'LogRecord' attributes (asctime, levelname, funcName, lineno).
- Employs classic Python string interpolation placeholders ('%s' for strings, '%d' for integers).
- Investigates the implicit conversion of module-level functions into proxy calls to the 'root' Logger instance.
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] | [%(levelname)s] | [%(funcName)s] (%(lineno)d) -> %(message)s",
)


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

    coffee_machine.activation()  # [2026-06-23 17:42:20,773] | [INFO] | [activation] (11) -> Coffee machine is starting up
    coffee_machine.scan()  # [2026-06-23 17:42:20,773] | [DEBUG] | [scan] (14) -> Checking the details...
    coffee_machine.cups_emptied()  # [2026-06-23 17:42:20,773] | [WARNING] | [cups_emptied] (17) -> We're running out of cups
    coffee_machine.machine_bolt()  # [2026-06-23 17:42:20,774] | [CRITICAL] | [machine_bolt] (23) -> The coffee machine is broken!

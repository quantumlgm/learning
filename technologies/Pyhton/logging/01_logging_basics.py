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

    coffee_machine.cups_emptied() # WARNING:root:We're running out of cups
    coffee_machine.machine_bolt() # CRITICAL:root:The coffee machine is broken!
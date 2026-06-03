# Design an abstract base class `BasePayment`, two subclasses 
# `StripePayment` and `PayPalPayment`, and a manager class `CheckoutManager` 
# to demonstrate polymorphism and abstract method behavior in Python.

# Requirements:
# 1. Base Class `BasePayment`:
#    - Implement an abstract method for processing payment that accepts 
#      an amount.
#    - This method must strictly raise a NotImplementedError to force 
#      subclasses to override it.

# 2. Subclasses `StripePayment` and `PayPalPayment`:
#    - Inherit from `BasePayment`.
#    - Override the payment processing method to return specific success 
#      messages containing the amount.

# 3. Manager Class `CheckoutManager`:
#    - Does NOT inherit from the payment classes.
#    - Accepts any payment object via its constructor.
#    - Implement a checkout execution method that triggers the payment 
#      processing on the stored payment object uniformly, 
#      demonstrating polymorphism.


class BasePayment:    
    def process_payment(self, amount: int) -> None:
        raise NotImplementedError('The method must be overridden in all subclasses')
    
class StripePayment(BasePayment):
    def process_payment(self, amount: int) -> str:
        return f"Stripe successfully processed the payment of {amount}"
    
class PayPalPayment(BasePayment):
    def process_payment(self, amount: int) -> str:
        return f"PayPal securely transferred {amount}"
    
class CheckoutManager():
    def __init__(self, payment_system: BasePayment) -> None:
        self.payment_system = payment_system

    def execute_checkout(self, amnout: int) -> str:        
        return self.payment_system.process_payment(amnout)

if __name__ == '__main__':
    base = BasePayment()
    # print(base.process_payment()) # NotImplementedError: The method must be overridden in all subclasses
    stripe = StripePayment()
    print(stripe.process_payment(1000)) # Stripe successfully processed the payment of 1000

    paypal = PayPalPayment()
    print(paypal.process_payment(2000)) # PayPal securely transferred 2000

    manager = CheckoutManager(paypal)
    print(manager.execute_checkout(1000)) # PayPal securely transferred 1000
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
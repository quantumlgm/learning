# Design a base class `BaseVault` and a subclass `SubVault` to demonstrate 
# how private and protected attributes behave during inheritance.

# Requirements:
# 1. Base Class `BaseVault`:
#    - Initialize with a vault name and a master key.
#    - Restrict access to the vault name from the outside, but keep 
#      it accessible for subclasses.
#    - Strictly isolate the master key from both external access and subclasses.
#    - Implement an internal validation method to verify if a given 
#      string matches the master key.

# 2. Subclass `SubVault`:
#    - Implement a method to return a string containing the vault's name 
#      accessed from the parent's attribute.
#    - Implement an access method that safely uses the parent's validation logic. 
#      Return "Access granted" or "Access denied" accordingly.
#    - Implement a simulation method that attempts to directly break into the 
#      parent's hidden master key to test encapsulation limits.
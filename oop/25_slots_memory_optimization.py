# Design an optimized base class `MassUnit` using `__slots__` and a 
# flexible subclass `HeroUnit` to demonstrate how Python handles memory 
# optimization and attribute restrictions.

# Requirements:
# 1. Class `MassUnit`:
#    - Use `__slots__` to restrict attributes strictly to 'x', 'y', and 'hp'.
#    - Implement an initializer to set these three attributes.
#    - Implement a `move(dx, dy)` method to update coordinates in-place.

# 2. Subclass `HeroUnit`:
#    - Inherit from `MassUnit`.
#    - Do NOT define `__slots__` in this subclass, allowing Python to automatically 
#      re-enable `__dict__` for dynamic attributes.
#    - Implement an initializer that sets base attributes via the parent 
#      class and adds a custom 'name' attribute.

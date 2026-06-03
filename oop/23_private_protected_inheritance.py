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


class BaseVault:
    def __init__(self, name: str, key: str) -> None:
        self._name = name
        self.__key = key
    
    def _check_key(self, key: str) -> None:
        return key == self.__key
    

class SubVault(BaseVault):
    def __init__(self, name: str, key: str) -> None:
        super().__init__(name, key)
    
    def get_name(self) -> None:
        return self._name
    
    def open_safe(self, key: str) -> None:
        if super()._check_key(key):
            return 'Acces granted'
        return 'Access denied'
    
    def hack(self):
        return self.__key


if __name__ == '__main__':
    base = BaseVault('base', 'base_key')
    sub = SubVault('sub', 'sub_key')
    print(sub.__dict__) # {'_name': 'sub', '_BaseVault__key': 'sub_key'}

    print(sub.get_name()) # sub
    print(sub.open_safe('another_key')) # Access denied
    print(sub.open_safe('sub_key')) # Access granted
    # print(sub.hack()) # AttributeError: 'SubVault' object has no attribute '_SubVault__key'. Did you mean: '_BaseVault__key'?
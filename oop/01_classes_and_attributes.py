"""
Design a class named `EnvironmentConfig` that acts as a dynamic and secure configuration manager for an application.

Requirements:
1. The ` __init__` method must accept two parameters:
   - `defaults` (dict): A dictionary containing initial configuration keys and values.
   - `readonly_keys` (tuple/list): A collection of attribute names that cannot be modified or deleted after initialization.

2. During initialization, the class must dynamically turn all keys from the `defaults` dictionary into object attributes using built-in Python functions.

3. Implement a method `update_config(self, new_settings: dict) -> None` that safely iterates through the dictionary and updates or adds attributes. 

4. Security constraints:
   - If a user attempts to delete a protected attribute (from `readonly_keys`), the deletion must be intercepted and prevented.
   - If a user attempts to overwrite a protected attribute with a new value, the modification must be ignored, keeping the original value intact.
   - If a user requests a non-existent attribute, instead of raising an AttributeError, the system should gracefully return the string "NOT_FOUND".

5. Use standard Python built-in tools for attribute manipulation: `getattr()`, `setattr()`, `hasattr()`, `delattr()`. 
Do not implement custom dunder methods like `__getattr__` or `__setattr__` yet, rely entirely on standard functions within your custom logic.
"""

class EnviromentConfig:
    def __init__(self, defaults, readonly_keys):
        for key, value in defaults.items():
            setattr(self, key, value)
        self.readonly_keys = readonly_keys
        print('Succesfully create')

    def get_config(self, key):
        print(getattr(self, key, "NOT_FOUND"))
    
    def set_config(self, new_dict):
        for key, value in new_dict.items():
            setattr(self, key, value)
            print(f'Successfully add: {key}: {value}')

    def update_config(self, key, value) -> None:
        if self.__dict__[key]:   
            if key not in self.readonly_keys:         
                setattr(self, key, value)
                print('Successfully update')
            else:
                print('Item in the private list')           

    def del_config(self, key):
        if self.__dict__[key]:
            if key not in self.readonly_keys:         
                delattr(self, key)
                print('Successfully delete')
            else:
                print('Item in the private list')
            
if __name__ == '__main__':
    Enviroment = EnviromentConfig({'set1': 1, 'set2': 2}, ('set1')) # Succesfully create
    Enviroment.get_config("set1") # 1
    Enviroment.set_config({'set3': 3, 'set4': '4'}) # Successfully add: set3: 3 and Successfully add: set4: 4
    Enviroment.update_config('set3', 30) # Successfully update
    Enviroment.update_config('set1', 10) # Item in the private list
    Enviroment.del_config('set3') # Successfully delete
    Enviroment.del_config('set1') # Item in the private list



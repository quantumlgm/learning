"""
Design a class named `UserProfile` that utilizes the `@property` decorator to 
manage access to a user's credentials with validation and data masking.

Requirements:
1. Initialization:
   - Accepts `username` (str) and `password` (str).

2. Username Property:
   - Implement getter and setter for the username.
   - The setter must ensure the value is a non-empty string. Invalid changes 
     must be ignored.

3. Password Property:
   - Implement getter and setter for the password.
   - The setter must simulate hashing/encryption: reverse the input string 
     and wrap it with asterisks (e.g., "hello" becomes "*olleh*"). Store 
     this masked string in a private attribute.
   - The getter must NEVER reveal the stored password. Any attempt 
     to read the password property must return the masked string "********".
"""


class UserProfile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def check_instance(self, item) -> bool:
        return isinstance(item, str) and len(item)            

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, new_username: str) -> None:
        if self.check_instance(new_username):
            self._username = new_username
        
    @property
    def password(self) -> str:
        return '********'
    
    @password.setter
    def password(self, new_password: str) -> None:
        if self.check_instance(new_password):
            self.__password = f'*{new_password[::-1]}*'
    

if __name__ == "__main__":
    Profile = UserProfile('Quantumlgm', 'secret123')
    print(Profile.__dict__) # {'username': 'Quantumlgm', '_UserProfile__password': 'secret123'}

    Profile.username = 'Ruslan'
    print(Profile.__dict__) # {'username': 'Ruslan', '_UserProfile__password': 'secret123'}

    Profile.password = 'newparol321'
    print(Profile.__dict__) # {'username': 'Ruslan', '_UserProfile__password': '*123lorapwen*'}

    Profile.name = ''
    print(Profile.__dict__) # {'username': 'Ruslan', '_UserProfile__password': '*123lorapwen*'}
    
    
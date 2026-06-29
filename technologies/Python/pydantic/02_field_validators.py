"""
Lesson 2: Pydantic Field Validators and Execution Order

Short Description:
Implementing field-level logic using @field_validator and inspecting context via ValidationInfo.

Detailed Description:
This module demonstrates sequential field validation mechanics in Pydantic V2:
- Utilizes '@field_validator' paired with '@classmethod' to evaluate individual inputs.
- Enforces a length constraint on the 'username' field.
- Demonstrates data flow dependency by anchoring 'confirm_password' validation AFTER
  'password' is processed, extracting the pre-validated value from 'info.data'.
"""

from pydantic import BaseModel, field_validator, ValidationInfo
from pprint import pprint


class UserRegistration(BaseModel):
    username: str
    password: str
    confirm_password: str

    @field_validator("username")
    @classmethod
    def username_validate(cls, username: str) -> str:
        if len(username) < 3:
            raise ValueError("Username must be more than 3 characters long")
        return username

    @field_validator("confirm_password")
    @classmethod
    def password_validate(cls, confirm_password: str, info: ValidationInfo) -> str:
        original_password = info.data.get("password")
        if original_password != confirm_password:
            raise ValueError(
                "The password you entered and the one you confirmed do not match"
            )
        return confirm_password


if __name__ == "__main__":
    user_valid = UserRegistration(
        username="Ruslan",
        password="protectparol2009",
        confirm_password="protectparol2009",
    )

    pprint(user_valid)
    """
    UserRegistration(
    username='Ruslan', 
    password='protectparol2009', 
    confirm_password='protectparol2009')
    """
    try:
        error_user = UserRegistration(
            username="Er", password="Ro", confirm_password="Rr"
        )
    except ValueError as e:
        print(e)  # 2 validation errors for UserRegistration

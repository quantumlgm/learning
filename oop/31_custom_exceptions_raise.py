# Upgrade the `RobotSpeedController` and its custom exceptions to professional production standards by adding state tracking inside exceptions and dynamic speed management.

# Requirements:
# 1. Custom Exceptions with State:
#    - `NegativeSpeedError(Exception)`: Implement `__init__(self, speed: int)`. 
#      Pass a formatted message to super(): "Invalid speed: {speed}. 
#      Speed cannot be negative".
#    - `SpeedTooHighError(Exception)`: Implement `__init__(self, speed: 
#      int, max_limit: int = 100)`. Calculate the exceeded delta. Pass to 
#      super(): "Speed {speed} km/h exceeds limit by {delta} km/h! Systems at risk".

# 2. Enhanced `RobotSpeedController`:
#    - Keep `_current_speed` initialized to 0.
#    - Refactor `set_speed(speed: int) -> None`: Pass the invalid speed value 
#      into the corresponding custom exception when raising.
#    - Implement `accelerate(value: int) -> None`: Calculate `new_speed`. 
#      Validate it using the same rules (raise errors if invalid). 
#      If valid, update `_current_speed`.
#    - Implement `emergency_brake() -> None`: Resets `_current_speed` 
#      to 0 instantly.


class SpeedTooHightError(Exception):
    def __init__(self, speed: int, max_limit: int = 100, *args):
        exceeded = speed - max_limit
        error_info = f"Speed {speed} km/h exceeds limit by {exceeded} km/h! Systems at risk"
        super().__init__(*args, error_info)

class NegativeSpeedError(Exception):
    def __init__(self, speed: int, *args):
        self.error_info = f"Invalid speed: {speed}. Speed cannot be negative"
        super().__init__(self, self.error_info, *args)


class RobotSpeedController:
    def __init__(self):
        self._current_speed = 0
    
    def validation(self, item):
        if item < 0:
            raise NegativeSpeedError('Speed cannot be negative')
        if item > 100:
            raise SpeedTooHightError("Speed limits exceeded! Systems at risk")

    def set_speed(self, speed: int) -> None:
        self.validation(speed)
        self._current_speed = speed

    def accelerate(self, value: int) ->  None:
        new_speed = self._current_speed + value
        self.validation(new_speed)

    def emergency_brake(self) -> None:
        self._current_speed = 0








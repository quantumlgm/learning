"""
Design a class named `ConnectionManager` that simulates a network connection lifecycle.
The class must automate connection tracking during initialization and ensure proper
cleanup when the object is destroyed.

Requirements:
1. Class Attributes:
   - `active_connections` (int): A counter tracking total alive connections,
      initialized to 0.

2. Instance Initialization (`__init__`):
   - Accepts two mandatory parameters: `ip_address` (str) and `port` (int).
   - Sets an instance attribute `is_connected` to True.
   - Increments the class-level `active_connections` counter by 1.
   - Prints a confirmation message containing the IP and port.

3. Instance Destruction (`__del__`):
   - Sets the instance attribute `is_connected` to False.
   - Decrements the class-level `active_connections` counter by 1.
   - Prints a termination message stating that the connection has been closed.

4. Methods to implement:
   - `get_status(self) -> tuple`: Returns a tuple containing the instance's
     `is_connected` status and the current class-level `active_connections` count.
"""


class ConnectionManager:
    active_connections = 0

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.is_connected = True

        type(self).active_connections += 1
        print(f"Connection successful: {ip_address}:{port}")

    def __del__(self):        
        type(self).active_connections -= 1
        print(f"Disconnection successful: {self.ip_address}:{self.port}")

    def get_status(self):
        return (self.ip_address, self.port, self.is_connected, type(self).active_connections)


if __name__ == "__main__":
    Connection1 = ConnectionManager("https://github.com/quantumlgm", "8888") # Connection successful: https://github.com/quantumlgm:8888
    print(f'Connection1: {Connection1.__dict__}') # 'is_connected': True
    print(ConnectionManager.__dict__) # ... 'active_connections': 1 ...

    Connection2 = ConnectionManager("https://localhost", "8000") # Connection successful: https://github.com/quantumlgm:8888
    print(f'Connection2: {Connection2.__dict__}') # 'is_connected': True
    print(ConnectionManager.__dict__)  # ... 'active_connections': 2 ...

    print(Connection1.get_status()) # ('https://github.com/quantumlgm', '8888', True)

    del Connection1
    print(ConnectionManager.__dict__) # 'active_connections': 1
    # Disconnection successful: https://github.com/quantumlgm:8888
    # Disconnection successful: https://localhost:8000    
"""
Task 32: Context Managers and the 'with' statement.

This program simulates a secure cloud video rendering session using a custom
context manager. It demonstrates the explicit control over resource allocation
and state management using the magic methods __enter__() and __exit__().

Key Features:
- Context Management: Guarantees that the server session is closed and memory
  is released, even if a runtime error occurs during the rendering process.
- State Tracking: Tracks cumulative memory usage across multiple frames and
  raises a MemoryError if the allocated server capacity is exceeded.
- Exception Handling: Safely intercepts exceptions in __exit__ to log the failure
  before propagating the error further up the call stack.
- Data Validation: Implements basic type checking for initialization and runtime
  arguments using static methods.
"""

def check_str(data: str):
    if not isinstance(data, str):
        raise TypeError("The data type must be a string")
    
def check_int(data: int):
    if not isinstance(data, int):
        raise TypeError("The data type must be a int")
    
class RenderEngine:
    effects = {

    }

    def __init__(self, memory_size: int) -> None:
        self.primary_memory = 0        
        self.memory_size = memory_size
    
    def render_frame(self, frame: int, memory: int, effect: str = None) -> None:
        check_int(frame)
        check_int(memory)
        check_str(effect)

        self.primary_memory += memory
        if self.primary_memory > self.memory_size:
            raise MemoryError("The server's memory is full")
        self.effects[frame] = effect
        print(
            f"Frame: {frame}, memory usage: {memory}, memory is used: {self.primary_memory}, effect: {self.effects[frame]}"
        )

    def current_effect(self, frame):
        try:
            print(f"Effect: {self.effects[frame]} is used")
        except KeyError:
            print("Effect: There are no effects in the current frame")

class SafetyConnection:
    def __init__(self, server_name: str, memory_size: int) -> None:
        check_str(server_name)
        check_int(memory_size)

        self.server_name = server_name
        self.memory_size = memory_size

    def __enter__(self):
        print(
            f"Successful connection to the {self.server_name} server. Memory reserved: {self.memory_size}"
        )
        return RenderEngine(self.memory_size)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.memory_size = None
        if exc_type:
            print(
                f"An error occurred during the operation: {exc_val}. However, the server session has been successfully closed"
            )
            raise
        print("Session is closed")


if __name__ == "__main__":
    print("Scenario A")
    with SafetyConnection("render-cluster-01", 512) as session:
        # Successful connection to the render-cluster-01 server. Memory reserved: 512
        session.current_effect(0)  # Effect: There are no effects in the current frame

        session.render_frame(
            1, 100, "noise"
        )  # Frame: 1, memory usage: 100, memory is used: 100, effect: noise
        session.current_effect(1)  # Effect: noise is used

        session.render_frame(
            2, 200, "HDR"
        )  # Frame: 2, memory usage: 200, memory is used: 300, effect: HDR
        session.current_effect(2)  # Effect: HDR is used
        # Session is closed

    print("\nScenario B")
    with SafetyConnection("render-cluster-02", 512) as session:
        # Successful connection to the render-cluster-02 server. Memory reserved: 512
        session.render_frame(
            1, 400, "Cinematic"
        )  # Frame: 1, memory usage: 400, memory is used: 400, effect: Cinematic
        session.render_frame(2, 200, "Cyberpunk")  # <- error occurrence
        print(
            "MemoryError: The server's memory is full"
        )  # MemoryError: The server's memory is full

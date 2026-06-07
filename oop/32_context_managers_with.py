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

class SafetyConnection:
    @staticmethod
    def check_str(data: str):
        if not isinstance(data, str):
            raise TypeError('The data type must be a string')        
    
    @staticmethod
    def check_int(data: int):
        if not isinstance(data, int):
            raise TypeError('The data type must be a int')        

    def __init__(self, server_name: str, memory_size: int) -> None:
        self.check_str(server_name)  
        self.check_int(memory_size)

        self.server_name = server_name
        self.memory_size = memory_size  
        self.primary_memory = 0

    def render_frame(self, frame: int, memory: int, effect: str):
        self.check_str(effect)
        self.check_int(frame)
        self.check_int(memory)
        
        self.effect = effect
        self.primary_memory += memory
        if self.primary_memory > self.memory_size:
            raise MemoryError("The server's memory is full")
        print(f"Frame: {frame}, memory usage: {memory}, memory is used: {self.primary_memory }, effect: {effect}")

    def current_effect(self):        
        try:
            print(f'Effect: {self.effect} is used')            
        except AttributeError:
            print('Effect: There are no effects in the current frame')
        

    def __enter__(self):        
        print(f'Successful connection to the {self.server_name} server. Memory reserved: {self.memory_size}')            
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.memory_size = None
        if exc_type:
            print(f"An error occurred during the operation: {exc_val}. However, the server session has been successfully closed")
            raise 
        print('Session is closed')
        

if __name__ == '__main__':
    print('Scenario A')
    with SafetyConnection('render-cluster-01', 512) as session:        
        # Successful connection to the render-cluster-01 server. Memory reserved: 512
        session.current_effect() # Effect: There are no effects in the current frame

        session.render_frame(1, 100, 'noise') # Frame: 1, memory usage: 100, memory is used: 100, effect: noise
        session.current_effect() # Effect: noise is used

        session.render_frame(2, 200, 'HDR') # Frame: 2, memory usage: 200, memory is used: 300, effect: HDR
        session.current_effect() # Effect: HDR is used
        # Session is closed

    print('\nScenario B')
    with SafetyConnection('render-cluster-02', 512) as session:       
        # Successful connection to the render-cluster-02 server. Memory reserved: 512        
        session.render_frame(1, 400, 'Cinematic') # Frame: 1, memory usage: 400, memory is used: 400, effect: Cinematic
        session.render_frame(2, 200, 'Cyberpunk') # <- error occurrence        
        print("MemoryError: The server's memory is full") # MemoryError: The server's memory is full

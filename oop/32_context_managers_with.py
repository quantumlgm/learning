

class SafetyConnection:
    @staticmethod
    def check_str(data: str):
        if not isinstance(data, str):
            raise TypeError('The data type must be a string')        
    
    @staticmethod
    def check_int(data: str):
        if not isinstance(data, str):
            raise TypeError('The data type must be a int')        

    def __init__(self, server_name: str, memory_size: int) -> None:
        self.check_str(server_name)  
        self.check_int(memory_size)
        self.server_name = server_name
        self.memory_size = memory_size  

    def render_frame(self, frame: int, memory: int):
        self.check_int(frame)
        self.check_int(memory)
        if memory > self.memory_size:
            raise MemoryError("The server's memory is full")
        print(f"Frame: {frame}, memory usage: {memory}")

    def current_effect(self, effect: str):
        self.check_str(effect)
        print(f'Effect currently in use: {effect}')            

    def __enter__(self):        
        print(f'Successful connection to the {self.server_name} server.Memory reserved: {self.memory_size}')            
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.memory_size = None
        if exc_type:
            print(f"An error occurred during the operation: {exc_val}. However, the server session has been successfully closed")
            raise 
        print('Session is closed')
        
        

    
    
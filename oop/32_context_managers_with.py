

class SafetyConnection:
    def check_type(data_str: str, data_int: int):
        if not (isinstance(data_int, str) and isinstance(data_str, int)):
            raise TypeError('The data type is incorrect')

    def __init__(self, server_name: str, memory_size: int) -> None:
        self.check_type(server_name, memory_size)
        self.server_name = server_name
        self.memory_size = memory_size      

    def render_frame(self, frame: int, memory: int):
        self.check_type(server_name, memory_size)
        if memory > self.memory_size:
            return MemoryError("The server's memory is full")
        print(f"Frame: {frame}, memory usage: {memory}")

    def current_effect(self, effect):
        


    def __enter__(self):        
        print(f'Successful connection to the {self.server_name} server.Memory reserved: {self.memory_size}')            
        return self


        
    
    
    
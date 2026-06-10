

class ClassChecker(type):
    def __new__(cls, name: str, bases: tuple, namespace: dict, **kwrd):
        for key in list(namespace.keys()):
            if not key.startswith('__'):
                value = namespace.pop(key)
                namespace[key.lower()] = value            

        if not name.startswith('API'):                
            raise NameError(f"The class '{name}' must start with 'API' prefix")
        
        
        namespace['_is_api_compliant'] = True
        super().__new__(cls, name, bases, namespace)


class APILoginHandler(metaclass=ClassChecker):
    def LoginUser():
        pass

    def Log_Out():
        pass


class BadUncheckedClass(metaclass=ClassChecker):
    pass    

        
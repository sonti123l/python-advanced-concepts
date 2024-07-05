def no_of_times(func):
    def Wrapper_function(*args,**kwargs):
        value = func(*args,**kwargs)
        for i in range(value):
            print("Hello World")
        return value
    return Wrapper_function  
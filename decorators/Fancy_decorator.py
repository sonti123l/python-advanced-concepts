from new_decorator import no_of_times
class FancyDecorators:
    def __init__(self,value):
        self.value = value
    
    @no_of_times
    def max_value(self,number_to_check):
        self._value = number_to_check
        return self._value 
    
Fancy_instance = FancyDecorators(5)

print(Fancy_instance.max_value(10))

# simple decorators are nothing but one function is passed as an argument to another function
#basically we use @ sign as the decorator to a decorated function which takes function as an argument
# #simple decorator underestanding 
def say_hello(func):
    def wrapper_function():
        print("It is a wrapper function")
        func()
        print("this wrapper function is acting locally inside the say_hello function")
        """so these functions are called with in a parent function they can't be called outside the parent class function"""
        """so to use these inside functions outside of that parent function we need to return that function by taking off that paranthesis because by returning function it directly called when called but by that we can assign that function to a variable"""
    return wrapper_function

def fucntion_to_be_called():
    print("It is a decorated function that is passed as a parameter to the parent class function")

#actual decorator calling be like this
fucntion_to_be_called = say_hello(func=fucntion_to_be_called)
print(fucntion_to_be_called) #it returns the value of the function addresss
fucntion_to_be_called()  ## it is called decorator calling function 

# output will be like It is a wrapper function
# It is a decorated function that is passed as a parameter to the parent class function
# this wrapper function is acting locally inside the say_hello function


# now we will see the @ sign at which it directly declares the statement of decorator creator
def say_hello(func):
    def wrapper_function():
        print("It is a wrapper function")
        func()
        print("this wrapper function is acting locally inside the say_hello function")
        """so these functions are called with in a parent function they can't be called outside the parent class function"""
        """so to use these inside functions outside of that parent function we need to return that function by taking off that paranthesis because by returning function it directly called when called but by that we can assign that function to a variable"""
    return wrapper_function

@say_hello
def fucntion_to_be_called():
    print("It is a decorated function that is passed as a parameter to the parent class function")




#the @ sign cretes the default decoration creation
# fucntion_to_be_called = say_hello(func=fucntion_to_be_called)
# print(fucntion_to_be_called) ## returns the function address
fucntion_to_be_called()  ## it is called decorator calling function

#now basically the decorator is consisting of properities,functions,classes and many more
#And for example if i wanted to get the name of the decorated function as the created function call 
#Then we need to use the functools package to get the decorated function as the name otherwise it gets the wrapper function as the name let's check it.
#with the function tools the name of the function by using __name__ we check the output..
from functools import wraps

def say_hello(func):
    @wraps(func)
    def wrapper():
        print("It is a wrapper function")
        func()
        print("this wrapper function is acting locally inside the say_hello function")
        """so these functions are called with in a parent function they can't be called outside the parent class function"""
        """so to use these inside functions outside of that parent function we need to return that function by taking off that paranthesis because by returning function it directly called when called but by that we can assign that function to a variable"""
    return wrapper

@say_hello
def fucntion_to_be_called():
    print("It is a decorated function that is passed as a parameter to the parent class function")

print(fucntion_to_be_called.__name__)

##output for this is
#fucntion_to_be_called

#we have different type of decorators in python 
# they are @property,@classmethod,@staticmethod 
#First one @property method is used for getter,setter to a class attributes we take an attribute value and get it as a property to that property we can change there value 
#Second @classmethod which used for a class to be called directly when this class method is called
#Third @staticmethod is used for that method which returns values doesn't change anytime
class Backer:
    def __init__(self,coin):
        self.coin = coin
        self.ruppees_counter = self.coin
        self._coins = 0

    @property
    def juice_machine(self):
        return self.coin*self.ruppees_counter

    @juice_machine.setter
    def juice_machine(self,coins):
        if coins >= self.coin:
            self._coins = coins*self.ruppees_counter
            return("Great have a nice coin") 
        else:
            return("Not having sufficient coins to get a coin Please check again...")

    @classmethod
    def call_this_class_method(cls):
        return cls(30)

    @staticmethod
    def pie():
        return f"pie value is {3.1474964}"

#creating an object for this 
user_came_for_juice = Backer(50)
# user_came_for_juice.juice_machine = 500
# user_message = user_came_for_juice.juice_machine
# print(user_message)

#class method calling 
user = Backer(30).call_this_class_method()
print(user.coin)
#class object address is assigned to a variable so that we can access the attributes and methods

#static emthod calling
print(user_came_for_juice.pie) #user_came_for_juice.pie this is returning the address of the function 
#calling that function keep the paranthesis





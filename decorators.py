# simple decorators are nothing but one function is passed as an argument to another function
#basically we use @ sign as the decorator to a decorated function which takes function as an argument
#simple decorator underestanding 
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

# Python decorators --> The beauty of syntaxic sugar '@'
import time


# Example of decorator function

def decorator_function(function):
    def wrapper_function():
        return function
    return wrapper_function()

def delay_function(function):

    def wrapper_function():
        time.sleep(3)
        function()
        function()
    return wrapper_function

@delay_function
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

say_hello()

wrap = delay_function(say_bye)
wrap()

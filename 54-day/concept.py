# Python decorators --> The beauty of syntaxic sugar '@'

# Example of decorator function

def decorator_function(function):
    def wrapper_function():
        return function
    return wrapper_function()


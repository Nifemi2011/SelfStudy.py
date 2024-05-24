# what is a scope? 
# A scope is a variable that can only be used in it's designated area.📦
Example:
#Local Scope: Variables within a function are local and exist only within that function.
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10


#Global Scope: Variables defined outside functions have global scope.
# Declare a global variable
message = "Hello"

def greet():
    # Access the global variable
    print("Local:", message)

greet()
print("Global:", message)



#Enclosing Scope: Nested functions can access variables from outer functions.
def outer(a):
    def inner():
        return a
    return inner

if __name__ == '__main__':
    inner_func = outer(10)
    print(inner_func())  # Output: 10


#Built-in Scope: Python provides built-in functions globally.
# Built-in scope example
print("Hello, world!")  # Output: Hello, world!

#@Nifemi_2011 @vscode
#@(c) Nifemi_2011

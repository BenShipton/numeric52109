###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

import numpy as np

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def sin(a):
    """Return the sin of a number in radians."""
    return np.sin(a)

def log(a):
    """Return the log base e of a number."""
    return np.log(a)



def calculator_interface():
    """Prompts the user for calculator input"""
    binary_operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    unary_operations = {
        "sin": sin,
        "log": log,
    }

    print("\n*** Simple Package Calculator ***")
    print("Valid operations: a + b, a - b, a * b, a / b")
    print("Enter 'exit' to quit.")

    while True:
        try:
            # Prompt the user for an input:
            user_input = input("Enter expression: ")

            # Check for exit
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                break

            parts = user_input.split()

            # Handle binary operations:
            if len(parts) == 3:
                arg1, op_symbol, arg2 = parts

                # Handle unknown operations:
                if op_symbol not in binary_operations:
                    print(f"Error: unknown operation symbol: {op_symbol}\n Please pick from {binary_operations}")
                    continue

                func = binary_operations[op_symbol]
                arg1 = float(arg1)
                arg2 = float(arg2)
                result = func(arg1, arg2)
                print(f"Result: {result}")

            # Handle unary operations:
            elif len(parts) == 2:
                op_symbol, arg1 = parts

                # Handle unknown operation symbol:
                if op_symbol not in unary_operations:
                    print(f"Error: unknown operation symbol: {op_symbol}\n Please pick from {unary_operations}")
                    continue
                
                func = unary_operations[op_symbol]
                arg1 = float(arg1)
                result = func(arg1)
                print(f"Result: {result}")
                
            else:
                print("Error: Invalid input format. Expected 'a op b' or 'op a'.")


        except ValueError:
            print("Error: Invalid number or argument (e.g., cannot convert text to number, or invalid math domain like negative square root). Please try again.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please try again.")
        except Exception as e:
            # Catches unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # This allows you to test the interface directly by running 'python operations.py'
    calculator_interface()
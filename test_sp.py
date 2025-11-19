###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package.operations as sp
import simple_package.statistics as st
import simple_package.graphics as gr
import numpy as np

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")


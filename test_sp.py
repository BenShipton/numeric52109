###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package.operations as sp
import simple_package.statistics as st

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")

    print(sp.sin(a))

    data = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 100.0]

    data = st.validate_and_convert_data(data)
    st.calculate_and_display_stats(data)


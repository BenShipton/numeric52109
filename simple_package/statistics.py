###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

# --- Dependency Check and Import ---
try:
    import numpy as np
    from numpy import mean, median, std
except ImportError:
    # Requirement 5: Handle missing NumPy
    raise ImportError("NumPy package is required for 'statistics.py'. Please install it using 'pip install numpy'")

# --- Core Functions ---

def validate_and_convert_data(data):
    """
    Validates the input data type and converts it to a NumPy array if necessary.
    
    Args:
        data (list or np.ndarray): The input data.
        
    Returns:
        np.ndarray: The validated and converted data.
        
    Raises:
        TypeError: If the input is neither a list nor a NumPy array.
    """
    # Requirement 4: Check that the input is a NumPy array or a list
    if isinstance(data, list):
        # Convert list to NumPy array
        data_array = np.array(data)
    elif isinstance(data, np.ndarray):
        data_array = data
    else:
        # Throw an exception if the type is invalid
        raise TypeError("Input data must be a Python list or a NumPy array.")
    
    # Check if the array contains numerical data (optional but good practice)
    if data_array.dtype.kind not in 'biufc': # B-boolean, I-integer, U-unsigned, F-float, C-complex
        raise ValueError("Input data must contain numerical values.")
        
    return data_array


def calculate_and_display_stats(data):
    """
    Calculates the mean, median, and standard deviation of the data,
    and displays the results in a clear format.
    
    Args:
        data (list or np.ndarray): The input data set.
        
    Returns:
        dict: A dictionary containing the calculated statistics.
    """
    try:
        data_array = validate_and_convert_data(data)
    except Exception as e:
        print(f"Error in data processing: {e}")
        return None

    # Requirement 1: Calculate the mean, median, and standard deviation
    data_mean = mean(data_array)
    data_median = median(data_array)
    data_std = std(data_array)

    results = {
        'mean': data_mean,
        'median': data_median,
        'std_dev': data_std,
        'data_array': data_array # Returning the array for potential plotting
    }

    # Requirement 2: Display the result with a clear and pretty print statement
    print("\n--- Statistical Analysis Results ---")
    print(f"Total Data Points: {len(data_array)}")
    print(f"  Mean (Average): {data_mean:.4f}")
    print(f"  Median (Middle): {data_median:.4f}")
    print(f"  Standard Deviation: {data_std:.4f}")
    print("------------------------------------\n")

    return results

if __name__ == '__main__':
    # Example usage:
    test_list = [10, 12, 23, 23, 16, 23, 21, 16]
    calculate_and_display_stats(test_list)

###
## simple_package - Module statistics.py
## Basic statistics plotter
###

# --- Dependency Check and Import ---
try:
    import matplotlib.pyplot as plt
    import numpy as np 
    # Import the necessary functions from your statistics module
    from .statistics import validate_and_convert_data 
    from numpy import mean, median # Import mean and median from numpy for internal calculation
except ImportError as e:
    # Requirement 5: Handle missing dependencies
    # The statistics module already checks for numpy, but we check for matplotlib here.
    if "matplotlib" in str(e):
        raise ImportError("Matplotlib package is required for 'graphics.py'. Please install it using 'pip install matplotlib'")
    else:
        # Re-raise any other ImportError (likely NumPy)
        raise


def plot_data_histogram(data, title="Data Histogram"):
    """
    Plots a histogram of the data, calculating the mean and median internally,
    and marking them on the plot.
    
    Args:
        data (list or np.ndarray): The data to plot.
        title (str): The title of the plot.
        
    Raises:
        TypeError, ValueError: If data validation fails.
    """
    
    # 1. Validate and Convert Data (using logic from statistics.py)
    data_array = validate_and_convert_data(data)
    
    # 2. Calculate Mean and Median
    data_mean = mean(data_array)
    data_median = median(data_array)
    
    # 3. Plotting Logic
    
    plt.figure(figsize=(10, 6))
    
    # Plot the histogram
    plt.hist(data_array, bins='auto', alpha=0.7, rwidth=0.85, color='skyblue', edgecolor='black', label='Data Frequency')
    
    # Mark the mean
    plt.axvline(data_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean ({data_mean:.2f})')
    
    # Mark the median
    plt.axvline(data_median, color='green', linestyle='dashdot', linewidth=2, label=f'Median ({data_median:.2f})')
    
    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    
    # Display the plot
    plt.show()
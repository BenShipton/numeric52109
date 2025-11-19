#######################
# Demo File
#######################
# This file demonstrates the use of the package "simple_package"
# The package contains 3 modules, graphics.py, operations.py, and statsitics.py

# Import the packages modules and numpy and matplotlib.pyplot:
import simple_package.operations as op
import simple_package.statistics as st
import simple_package.graphics as gr
import numpy as np
import matplotlib.pyplot as plt

def run_operations_demo():
    """
    Demonstrates the interactive calculator interface.
    """
    print("=============================================")
    print("       1. Operations Module Demo (Interactive) ")
    print("=============================================")
    print("NOTE: The calculator interface is interactive.")
    print("Try entering: '10 + 5', 'sqrt 81', 'log 2.718', or 'exit'.")
    op.calculator_interface()
    print("---------------------------------------------")


def run_statistics_and_graphics_demo():
    """
    Demonstrates the statistics calculation and histogram plotting.
    """
    print("=============================================")
    print("       2. Statistics and Graphics Demo         ")
    print("=============================================")

    # Sample Data for Demonstration
    # Note: We include an outlier (100) to show how mean and median differ.
    data_list = np.random.normal(0, 2, 100)
    
    print(f"Sample data (Python list): {data_list}")
    
    # 2a. Demonstration of statistics.py
    print("\n--- Running st.calculate_and_display_stats ---")
    stats_results = st.calculate_and_display_stats(data_list)
    
    if not stats_results:
        print("Skipping graphics demo due to calculation error.")
        return

    # 2b. Demonstration of graphics.py
    if plt:
        print("--- Running gr.plot_data_histogram ---")
        print("A histogram plot should now appear, marking the mean and median.")
        
        # The graphics function only requires the raw data and calculates stats internally
        gr.plot_data_histogram(data_list, title="Demo Data Distribution (Mean vs. Median)")
    else:
        print("\nSkipping gr.plot_data_histogram because Matplotlib is unavailable.")
        

if __name__ == '__main__':
    # Run the interactive calculator demo
    run_operations_demo()
    
    # Run the statistics and graphics demo
    run_statistics_and_graphics_demo()
    
    print("\nDemo Complete.")



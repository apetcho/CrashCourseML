#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import wraps

def title(msg):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            n = len(msg)
            dash = '*' * n
            print(f"\n{dash}\n{msg}\n{dash}\n\n")
            ans = func(*args, **kwargs)
            if ans is None:
                return
            return ans
        return wrapper
    return decorate
    

@title("Basic Plots")
def basic_plot():
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    z = np.cos(x)
    plt.figure()
    plt.plot(x, y, label='sinus', color='blue', linestyle='--', linewidth=2)
    plt.plot(x, z, label='cosinus', color='red', linestyle='--', linewidth=2)
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.title("Title")
    plt.legend()
    plt.show()
    

@title("Scatter 2D Plots")
def scatter_2d_plots():
    np.random.seed(2021)
    data = np.random.randn(2, 100)
    plt.scatter(data[0], data[1])
    plt.title("Scatter 2D Plot")
    plt.show()

def main():
    # basic_plot()
    scatter_2d_plots()
    
    
if __name__ == "__main__":
    main()
#!/usr/bin/python3

"""Write a NumPy program to test whether two arrays are element-wise equal within a tolerance."""

import numpy as np

if __name__ == "__main__":
    print("Test if two arrays are element-wise equal within a tolerance:")
    print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
    print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
    print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))
    print(np.allclose([1.0,np.nan], [1.0,np.nan]))
    print(np.allclose([1.0,np.nan], [1.0,np.nan], equal_nan=True))
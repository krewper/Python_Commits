#Python program that demonstrates various array creation techniques
import numpy as np

#creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print("Aray created using passed list:\n", a)

#creating array from tuple
b = np.array((1, 3, 2))
print("Array created using passed tuple:\n", b)

#creating a 3X4 array with all zeroes
c = np.zeros((3, 4))
print("\n An array initialised with all zeros:\n", c)

#creating a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print("\nAn array initialised with all 6s. Array type is complex:\n", d)

#create an array with random values
e = np.random.random((2, 2))
print("\nA randomly initialised array:\n", e)

#create a sequence of integers from 0 to 30 in steps of 5
f = np.arange(0, 30, 5)
print("\n A sequential array with steps of 5: \n", f)

#create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print("\n A sequential array with 10 values between 0 and 5: \n", g)

#Reshaping 3X4 array to 2X2X# array
arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)

print("\nOriginal array: \n", arr)
print("Reshaped array: \n", arr)

# FLatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print("\nOriginal array:\n", arr)
print ("Fattened array: \n", flarr)
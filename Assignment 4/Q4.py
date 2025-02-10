import numpy as np

Dhruv = np.linspace(10, 100, 25)

print("Array:", Dhruv)
print("Dimensions:", Dhruv.ndim) 
print("Shape:", Dhruv.shape)  
print("Total Elements:", Dhruv.size)  
print("Data Type of Elements:", Dhruv.dtype)  
print("Total Bytes Consumed:", Dhruv.nbytes)  


transposed_array = Dhruv.reshape(25, 1)
print("\nTransposed using reshape():\n", transposed_array)

print("\nTransposed using .T:\n", Dhruv.T) 

print("\nIs reshaped array same as .T? :", np.array_equal(transposed_array, Dhruv.T))
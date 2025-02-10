import numpy as np

arr3 = np.array([
    [10, 20, 30], 
    [40, 50, 60], 
    [70, 80, 90]
])

element_a = arr3[0, 1]  
element_b = arr3[2, 0]  

print("Element at 1st row, 2nd column:", element_a)
print("Element at 3rd row, 1st column:", element_b)  
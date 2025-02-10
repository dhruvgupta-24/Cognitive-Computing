ucs420_Dhruv = np.array([
    [10, 20, 30, 40], 
    [50, 60, 70, 80], 
    [90, 15, 20, 35]
])

mean_value = np.mean(ucs420_Dhruv)     
median_value = np.median(ucs420_Dhruv)  
max_value = np.max(ucs420_Dhruv)        
min_value = np.min(ucs420_Dhruv)         
unique_values = np.unique(ucs420_Dhruv)  

reshaped_ucs420_Dhruv = ucs420_Dhruv.reshape(4, 3)


resized_ucs420_Dhruv = np.resize(ucs420_Dhruv, (2, 3))

print("Original 3x4 Array (ucs420_Dhruv):\n", ucs420_Dhruv)
print("\nMean:", mean_value)
print("Median:", median_value)
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Unique Elements:", unique_values)

print("\nReshaped (4x3) Array:\n", reshaped_ucs420_Dhruv)
print("\nResized (2x3) Array:\n", resized_ucs420_Dhruv)
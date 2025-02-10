import numpy as np

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

unique, counts = np.unique(x, return_counts=True)

max_count_index = np.argmax(counts)
most_frequent = unique[max_count_index]

indices = np.where(x == most_frequent)[0]

print("Most Frequent Value in x:", most_frequent)
print("Indices of Most Frequent Value in x:", indices)
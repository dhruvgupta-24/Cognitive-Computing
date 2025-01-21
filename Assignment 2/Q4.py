
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

unique_scores = A.union(B)
print(f"Unique scores (Union): {unique_scores}")

common_scores = A.intersection(B)
print(f"Common scores (Intersection): {common_scores}")

exclusive_scores = A.symmetric_difference(B)
print(f"Exclusive scores (Symmetric Difference): {exclusive_scores}")

is_A_subset_B = A.issubset(B)
is_B_superset_A = B.issuperset(A)
print(f"Is Team A's scores a subset of Team B's scores? {is_A_subset_B}")
print(f"Is Team B's scores a superset of Team A's scores? {is_B_superset_A}")

X = int(input("Enter a score to remove from Team A's scores: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from Team A. Updated scores: {A}")
else:
    print(f"Score {X} is not present in Team A's scores.")
marks=(45, 89.5, 76, 45.4, 89, 92, 58, 45)

highest_score=max(marks)
highest_index=marks.index(highest_score)
print(f"Highest score is {highest_score} and its index is {highest_index}")

lowest_score=min(marks)
lowest_count=marks.count(lowest_score)
print(f"Lowest score is {lowest_score} and it appears {lowest_count} times")

reversed_list=list(reversed(marks))
print("Reversed tuple as a list: ",reversed_list)

a=int(input("Enter a number: "))
if a in marks:
    first_occur=marks.index(a)
    print(f"{a} is present at index {first_occur}")
else:
    print(f"{a} is not present")
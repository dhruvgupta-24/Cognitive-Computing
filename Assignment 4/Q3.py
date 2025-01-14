a=int(input("Enter a number: "))
i=1
sum=0
for i in range(1,a+1):
    sum=sum+i
    i+=1

print(f"Sum from 1 to {a} = {sum}")
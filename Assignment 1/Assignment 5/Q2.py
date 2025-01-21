a=int(input("Enter a number: "))

factorsum=0
i=1
for i in range(1,a):
    if(i%63==0):
        factorsum=factorsum+i
        i+=1

print(f"Sum of all number divisible by 7 and 9 from 1 to {a} = {factorsum}")
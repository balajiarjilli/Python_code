#A factor of a number is a number that divides the given number evenly or exactly, leaving no remainder. 

num = int(input("enter a number : "))
lst=[]
for i in range(1,int(num/2)+1):
    if num%i == 0:
        lst.append(i)
print(lst)
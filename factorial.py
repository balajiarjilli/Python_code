num = int(input("enter a number : "))
s = num
for i in reversed(range(1,num)):
    s = s*i
print(s) 
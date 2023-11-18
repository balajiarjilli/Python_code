#number divisible by one and itself
num = int(input("enter a number: "))
if num == 1:
    print(f"the number {num} is not a prime number")

for i in range(2,num):
    if num%i != 0 or num==2:
        print(f"the number {num} is  prime number")
        break
    else:
        print(f"the number {num} is not a prime number")
        break


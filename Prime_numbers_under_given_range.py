x =100
prime=[]
non_prime=[]
for n in range(1,x+1):
    flag = 1   # prime
    if n==1:
        flag = 0    # non prime    
    else:
        for i in range(2,n):
            if n%i == 0:
                flag = 0
                break
    
    if flag == 0:
        non_prime.append(n)
    else:
        prime.append(n)

print("list of prime number", prime)
print("list of non prime number",non_prime)

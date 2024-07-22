def isPrime(num):
    i = 2
    while i*i<=num:
        if num%i==0:
            return False
        i += 1

    return True
ans = isPrime(17) 
print(ans)

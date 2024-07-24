n = int(input("Enter an int no."))
prime = []
for i in range(n+1):
    prime.append(i)

prime[0]=0
prime[1]=0

p = 2
while (p * p <= n): 
    if (p != 0 ):
        for i in range(p*2,n+1,p):
            prime[i] = 0

    p += 1

print("All the prime number up to", n, "are:")
for i in range(len(prime)):
    if (prime[i] !=0 ):
        print(prime[i], end=" ")

print()
print(prime)
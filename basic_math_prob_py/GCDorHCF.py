# GCD or HCF

def gcd(a,b):
    divisor = min(a,b)
    dividend = max(a,b)

    while dividend % divisor != 0:
        temp = dividend
        dividend = divisor
        divisor = temp % divisor
    return divisor

ans = gcd(12,15)
print(ans)






'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b # uses the Euclidean algorithm, 
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD/HCF
result = gcd(num1, num2)

# Print the result
print(f"The GCD/HCF of {num1} and {num2} is {result}.")

'''


































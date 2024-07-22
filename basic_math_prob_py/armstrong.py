def countNumber(num):
    return len(str(num))

def armstrong(num):
    ans = 0

    k = countNumber(num)
    temp = num
    while num > 0:
        rem = num % 10
        ans = ans + rem ** k
        num = num // 10

    return temp == ans 

num = int(input("Enter the number: "))
ans = armstrong(num)
if ans: 
    print(f"{num} is an Armstrong number: {ans}")
else: 
    print("no. is not armstrong")

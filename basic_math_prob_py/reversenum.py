# reverse the number

def reverseno(num):
    ans = 0
    while num > 0:
        rem = num%10
        ans = ans * 10 + rem
        num = num // 10
    return ans


num = int(input('enter the numbers:'))
ans = reverseno(num)
print('the reverse of the number is ',ans)



'''
def reverse_number(num):
    # Convert the number to a string, reverse the string, and convert it back to an integer
    reversed_num = int(str(num)[::-1])
    return reversed_num

# Input a number
num = int(input("Enter a number: "))

# Get the reversed number
reversed_num = reverse_number(num)

# Print the reversed number
print("Reversed number:", reversed_num)


'''
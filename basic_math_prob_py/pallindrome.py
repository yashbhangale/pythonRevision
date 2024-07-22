# # 121 = 121 = pallindrome

# def reverseno(num):
#     ans = 0
#     while num > 0:
#         rem = num%10
#         ans = ans * 10 + rem
#         num = num // 10
#     return ans


# def pallindrome(num):
#     return num == reverseno(num)


# num = int(input('enter the numbers:'))
# ans = num
# ans = pallindrome(num)
# print(ans)


def reverseno(num):
    num = int(str(num)[::-1])
    return num

def pallindrome(num):
    return num == reverseno(num)

num = int(input('Enter the number:'))

# Check if the number is a palindrome using if-else
if pallindrome(num):
    print("The number is a palindrome.",num)
else:
    print("The number is not a palindrome.")


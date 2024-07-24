# check if a string is palindrome or not

# palindrome = lambda s: s == s[::-1]
# print(palindrome("yash"))
# print(palindrome("madam"))


string = input("Enter a string: ")
def is_palindrome(string, s, e):
    if s >= e:
        return True
    if string[s] != string[e]:
        return False
    return is_palindrome(string, s + 1, e - 1)

ans = is_palindrome(string, 0, len(string) - 1)
print(ans)







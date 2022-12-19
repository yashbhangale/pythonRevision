# recursion is a function that calls itself
# recursion is a way to solve problems that can be broken down into smaller versions of the same problem
# recursion example: factorial

def factorial (n):
    if n < 2:
        return 1
    return n * factorial(n-1)





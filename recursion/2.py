# Print 1 to n using recurion
def printOtoN(i,n):
    if i > n:
        return
    print(i)
    printOtoN(i+1,n)

printOtoN(1,7)
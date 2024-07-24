# Print n to 1 using recursion 
def PrintOtoN(i,n):
    if i > n:
        return
    PrintOtoN(i+1,n)
    print(i)

PrintOtoN(2,7)
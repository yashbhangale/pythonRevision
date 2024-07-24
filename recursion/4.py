# sum of first n numbers
def sumN(i,n):
    if i>n:
        return 0
    ans = sumN(i+1,n)+i
    return ans
ans = sumN(1,5)    
print(ans)
    
# reverse an array (list)
lst = list(map(int,input().split()))
n = len(lst)
s=0
e= n-1

while s<=0:
    lst[s],lst[e]=lst[e],lst[s]
    s+=1
    e-=1
print(lst)



# with recusrion function
'''
def reverse_list(lst, s, e):
    if s >= e:
        return
    lst[s], lst[e] = lst[e], lst[s]
    reverse_list(lst, s + 1, e - 1)

lst = list(map(int, input().split()))
reverse_list(lst, 0, len(lst) - 1)
print(lst)

'''

### Square Pattern
```
n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

### Right triangle of stars pattern

```
n = 5 

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()     
```

### Right triangle of numbers pattern

```
n = 5 

for i in range(n):
    for j in range(i+1):
        print(j + 1, end=" ")
    print()     

```

### Right triangle of repeated numbers pattern

```
n = 5 

for i in range(n):
    for j in range(1,i+2):
        print(i + 1, end=" ")
    print()    
```

### Inverted Right triangle of stars pattern


```
n = 5 
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
```

### Inverted Right triangle of numbers pattern


```
n = 6

for i in range(n):
    for j in range(1,n-i):
        print(j+i,end=" ")
    print()
```
### Pyramid of stars pattern

```
n = 5
for i in range(n):
    for j in range(n-1-i):
        print("", end=" ")
    for j in range (2*i+1):
        print("*",end="")
    print()
```

### Inverted Pyramid of stars pattern

```
n = 5

for i in range(n):
    for j in range(i):
        print("", end=" ")
    for j in range (2*(n-1-i)+1):
        print("*",end="")
    print()
```

### Diamond of stars pattern

```
n = 5 

for i in range (2*n):
    if i < n:
        for j in range( i+1 ):
            print("*",end=" ")
    else:
        for j in range (i,2*n-1):
            print("*",end=" ")
    print() 
```

### Alternate pattern of 0 and 1

```
n = 5 
for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2,end =" ")

    print()
```

### Number pattern with spaces

```
n = 4 
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range ((n-i-1)*2):
        print(" ", end = " ")
    for j in range (i+1,0,-1):
        print(j, end = " ")
    print()
```

### Continuous number pattern

```
n = 5
k = 1
for i in range(n):
    for j in range(i+1):
        print(k,end="")
        k += 1
    print()
```
### Alphabetic pattern

```
n = 5
def nummToChr(num):
    return chr(num + 65)

for i in range(n):
    for j in range(i+1):
        print(nummToChr(j),end=" ")
    print()        
```

### Inverted Alphabet Pattern

```
def nummToChr(num):
    return chr(num + 65)
n = 5
k = n-1 
for i in range(n):
    for j in range(i+1):
        print(nummToChr(k+j),end=" ")
    k-=1
    print()        
```













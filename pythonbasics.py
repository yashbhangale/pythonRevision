print("hello world")
print("hello coders")


# variables in python 
# variables are used to store data
# we can change the value of the variable


name = "yash"
age = 19
print(name,age)
is_adult = True

# python is case sensitive
#strings in python
# strings are used to store text ("hello world")

# four ways to write strings
# string , number , boolean (true or false), list


# input function in python
# input function is used to take input from the user
# input function always returns a string
name = input("what is your name ? ")
print("hello",name)  # concatenation of strings using comma (,) 


# type conversion in python 
# type conversion is used to convert one data type to another data type

old_age = input("what is your old age ? ")
new_age = int(old_age) + 2
print(new_age) # type error because we can't add string and integer 

# int() # int() is used to convert string to integer
# float() # float() is used to convert string to float
# float is used to store decimal values

# str() # str() is used to convert integer to string
# bool() # bool() is used to convert integer to boolean





####################################
#sum of two numbers

first = input("enter first number : ")
second = input("enter second number : ")

sum = int(first) + int(second)
#sum = first + second

print("the sum is : " + str(sum))


#################################~

name = "batman"
print(name.upper()) # BATMAN
print(name.lower()) # batman
print(name.title()) # Batman
print(name.capitalize()) # Batman
print(name.find("a")) # 1
print(name.find("l")) # -1
# index is used to find the index of the character which start from 0

#replace exisiting string with new string
print(name.replace("batman","superman")) # superman

#keyowrds in python 
#keywords are reserved words in python

# for eg print, input, int, float, str, bool, if, else, elif, for, while, break, continue, pass, return, def, class, try, except, raise, assert, import, from, as, global, nonlocal, lambda, True, False, None, and, or, not, is, in, del, with, as, yield, async, await

# infunction in python
print("batman" in name) # True

# operators in python
# operators are used to perform operations on variables and values
# + , - , * , / , % , ** , // , += , -= , *= , /= , %= , **= , //= , == , != , > , < , >= , <= , is , is not , in , not in , not , and , or
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5%2) # modulus operator (remainder)
print(5**2) # power operator
print(5//2) # = 2 
# comparison operators in python 
# comparison operators are used to compare two values
# == , != , > , < , >= , <= , is , is not , in , not in
print(5==2) # 
print(5!=2)
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
#############################

# operator precedence

result = 20 - 10 / 5 * 3 ** 2 # 20 - 2 * 9 = 20 - 18 = 2
print(result)

# logical operators in python
# logical operators are used to combine conditional statements 

# if-else statement in python 
# if-else statement is used to execute a block of code if a condition is true

age = 19

if age >= 18:
    print("you are adult")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")
print("thank you")




# calculator program in python
first = int(input("enter first number : "))
operator = input("enter operator : ")
second = int(input("enter second number : "))

if operator == "+":
    print(int(first) + int(second))
elif operator == "+":
    print(int(first) + int(second))
elif operator == "+":
    print(int(first) + int(second))
elif operator == "+":
    print(int(first) + int(second))
elif operator == "+":
    print(int(first) + int(second))
else : 
    print("invalid operator")



# range function in python
numbers = list(range(1,10))
print(numbers)


# loops in python
# loops are used to execute a block of code multiple times
# while loop in python
# while loop is used to execute a block of code multiple times until a condition is true
i = 1
while i <= 100000000000000000000000000000000000000000000000000000000:
    print(i)
    i = i + 1 

# pattern printing program in python
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1 

i = 5 
while i >= 0:
    print(i * "*")
    i = i - 1


# for loop in python 
# for loop is used to execute a block of code multiple times until a condition is true
# for loop is used to iterate over a sequence (list, tuple, string, dictionary, set, range)
for i in range(1,11):
    print(i)
    
# list (data type ) in python 
# list is used to store multiple items in a single variable 
# list is a collection which is ordered and changeable. Allows duplicate members.
# list is created using square brackets []
# list is mutable (changeable) 

marks = [10,20,30,40,50,60,70,80,90,100]
print (marks)
print (marks[5])

# index can be negative in  python
print (marks[-1]) # 100
print (marks[-2]) # 90
print (marks[1:5]) # [20,30,40,50]
for score in marks:
    print(score)
    
# operations on list in python
# append() , insert() , remove() , pop() , clear() , index() , count() , sort() , reverse() , copy()

# append() is used to add an item at the end of the list

marks.append(110)
marks.insert(3, 35)
marks.remove(35)
marks(100 in marks)
print(len(marks))
marks.clear()
print(marks)

# break and continue in python
# break is used to stop the loop
# continue is used to skip the current iteration of the loop and continue with the next iteration

heros = ["batman","superman","wonderwoman","aquaman","flash","cyborg"]
for student in heros:
    if student == "cyborg":
        break
    print(student)





    






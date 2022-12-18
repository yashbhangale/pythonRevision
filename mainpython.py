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
print(5%2)
print(5**2)
print(5//2)
print(5==2)
print(5!=2)
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)












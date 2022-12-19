# for loop in python
for x in range (5):
    print(x) 
    
# range function
# range(start, stop, step)
# start: starting number of the sequence
# stop: generate numbers up to, but not including this number
# step: difference between each number in the sequence
# range function number start from 0


# example of for loop
friends = ["Jim", "Karen", "Kevin"] # list of friends using [] brackets (list)
for friend in friends:
    print("hello " + friend)



# example of for loop 2
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
length = 0
for value in values:
    sum+=value
    length+=1
    
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

#############################################################################

def to_celsius(x):  # def is  used to define a function
    return (x-32)*5/9  # return is used to return a value from a function

#############################################################################

for x in range(0,101,10):
    print(x, to_celsius(x))









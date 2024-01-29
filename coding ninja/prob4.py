'''
 Problem statement

Take the principal amount, rate of interest, and the time period as input and calculate the Simple Interest.

Note: Return answer as Floor integer value.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:

2000
2.2
4

Sample Output 1:

176

Explanation of Sample Input 1:

The input is principal=2000, rate=2.2 and time=4.
So Simple interest=Principal*rate*time/100 hence 
answer is 2000*2.2*4/100=176
'''

#code:

from math import floor

def calculate_simple_interest(principal, rate_of_interest, time_period):
    # Calculate Simple Interest using the formula: Principal * Rate * Time / 100
    simple_interest = (principal * rate_of_interest * time_period) / 100
    
    # Return the floor integer value of the result
    return floor(simple_interest)

# Taking input from the user
principal_amount = float(input(""))
rate_of_interest = float(input(""))
time_period = float(input(""))

# Calling the function and printing the result
result = calculate_simple_interest(principal_amount, rate_of_interest, time_period)
print(result)



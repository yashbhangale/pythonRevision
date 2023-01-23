# dictionary to store the squad

###############################################################
squad = {
    'Virat Kohli': 'Delhi , 31 , Batsman  ',
    'Rohit Sharma': 'Maharashtra , 32 , Batsman',
    'Shikhar Dhawan': 'Delhi , age:33 , Batsman',
    'KL Rahul': 'Karnataka , 26 , Batsman',
    'MS Dhoni': 'Jharkhand , 37, Batsman',
    'Hardik Pandya': 'Gujarat , 25 , allrounder',
    'Ravindra Jadeja': 'Gujarat, 30 , allrounder',
    'Bhuvneshwar Kumar': 'Uttar Pradesh , 29 , bowler',
    'Jasprit Bumrah': 'Gujarat , 25 , Bowler',
    'Yuzvendra Chahal': 'Haryana, 28 , Bowler',
    'Kedar Jadhav': 'Maharashtra, 34 , allrounder ',
    'Dinesh Karthik': 'Tamil Nadu , 33 , allrounder',
    'Vijay Shankar': 'Tamil Nadu , 28 , allrounder',
    'Mohammed Shami': 'Uttar Pradesh , 28 ,allrounder',
    'Kuldeep Yadav': 'Uttar Pradesh , 24 , allrounder'
}

# function for displaying names 
def display_state(name):
    if name in squad:
        print(f"{name} is from {squad[name]}")
    else:
        print(f"{name} is not in the squad")

# take user input with input() function
display_state(input())

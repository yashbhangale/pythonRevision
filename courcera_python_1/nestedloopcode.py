# nested for loop in python 
# nested for loop is a loop inside a loop

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print()
        
        
        
teams = ["ironman", "captain america", "superman", "Batman"]
for team_one in teams:
    for team_two in teams:
        if team_one != team_two:
            print(team_one + " vs " + team_two)
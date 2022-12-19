# break and continue statements in python is used to control the flow of the program

# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break

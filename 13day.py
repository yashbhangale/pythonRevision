
# time module is used to get the current time

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)




#########################################################################################
#greeting based on time (program)

import time
currentTime = time.strftime('%H:%M')   

if currentTime.hour < 12 :
     print('Good morning')
if currentTime.hour > 12 :
     print('Good afternoon')
if currentTime.hour > 6 :
     print('Good evening')
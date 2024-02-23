# weekday.py
# autor = Ianara Fernandes

weekday = ["monday",
"tuesday", 
"wendswday", 
"thursday", 
"friday", 
"saturday", 
"sunday"]

from datetime import datetime

# get current datetime
dt = datetime.now()
print('Datetime is:', dt)

# get weekday name
if "monday to friday":
 print('day Name:', dt.strftime('%A'), "Yes, unfortunately today is a weekday.") 

else: print('day Name:', dt.strftime('%A'), "It is the weekend, yay!" )
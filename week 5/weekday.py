# Week task 5 (when you run the program will ready the day of the week you are running and give you the answer, with date, time and weekday.
# Autor = Ianara Fernandes

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
 print(dt.strftime('%A'), "Yes, unfortunately today is a weekday.") 

else: print(dt.strftime('%A'), "It is the weekend, yay!")
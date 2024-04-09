students= []
def readModules():
 return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Andrew: ")  # Prompt for the student's name
    currentStudent["modules"] = readModules()
    
    students.append(currentStudent)

# Test
doAdd(students)
doAdd(students)
print(students)

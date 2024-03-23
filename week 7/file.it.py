import json
FILENAME ="testdict.json"
def readDict():
 # this will throw an error if the file does not exist
 # it should readly just return an empty dict
 # we can do this later
 with open(FILENAME) as f:
  return json.load(f)
# test the function
somedict = readDict()
print(somedict)


# after run show up this {'name': 'fred', 'age': 31, 'grades': [1, 34, 55]}
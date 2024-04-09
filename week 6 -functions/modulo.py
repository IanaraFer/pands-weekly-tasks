def readModules():
 modules = []
 moduleName = input("\tprogramming:").strip()
 
 while moduleName != "":
  module = {}
 module[""]= moduleName
 # I am not doing error handling
 module["grade"]=int(input("\t\t45:"))
 modules.append(module)
 # now read the next module name
 moduleName = input("\thistory").strip()
 return modules
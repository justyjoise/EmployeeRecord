'''
class Dog:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print(self.name +" is bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
'''
    
class Employee:
	def __init__(self, EmployeeID, EmployeeName,EmployeeLocation,EmployeeSalary):
		self.EmployeeID = EmployeeID
		self.EmployeeName = EmployeeName
		self.EmployeeLocation = EmployeeLocation
		self.EmployeeSalary = EmployeeSalary

	def GetEmployee(self):
		print(str(self.EmployeeID) + " , " + self.EmployeeName + " ,"+self.EmployeeLocation + " , " + str(self.EmployeeSalary))
        
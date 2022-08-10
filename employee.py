from secrets import choice
#https://www.youtube.com/watch?v=qJIy6o6uEE8&t=151s
class Employee: 
    employeeList = list()
    def __init__(self, empNo, empName, empDep, empSal):
        self.empNo, self.empName, self.empDep, self.empSal = empNo, empName, empDep, empSal   
     
    def addNewEmployee(self):   
        Employee.employeeList.append(self)
    
   
        
    def getEmpList(self):
        return Employee.employeeList
    
    def setEmpNo(self, empNo):
        self.empNo = empNo
    def getEmpNo(self):
        return self.empNo
    def setEmpName(self, empName):
        self.empName = empName
    def getEmpName(self):
        return self.empName
    def setempDep(self, empDep):
        self.empDep = empDep
    def getEmpDep(self):
        return self.empDep
    def setEmpSal(self, empSal):
        self.empSal = empSal
    def getEmpSal(self):
        return self.empSal
    def __str__(self):
        return "%d %s %s %d"%(self.empNo, self.empName, self.empDep, self.empSal)
    
# emp1 = Employee(1,"kark","developer", 300000)
# print(emp1)

choice = 1
employee = Employee(0," ", " ", 0.0)
while choice >= 1 and choice <= 2:
    print("\n\n1. Add New Employee\n2. Get all Employee List\n\n")
    choice = int(input("Enter your Choice: "))
    if(choice == 1 ):
        empNo = int(input("Enter Your Employee ID number: "))
        empName = input("Enter Employee Name: ")
        empDep = input("Enter Employee Department: ")
        empSal = float(input("Enter Employee Salary: "))
        emp = Employee(empNo, empName, empDep, empSal )
        emp.addNewEmployee()
    
    elif(choice == 2 ):
        print("\n")
        for emp in employee.getEmpList():
            print(emp)
    
    
    
<<<<<<< HEAD
# from secrets import choice
=======
from secrets import choice
>>>>>>> 1c31f22cbea733d1878d770e8ddab58788ed71cb

class Employee: 
    employeeList = list()
    def __init__(self, empNo, empName, empDep, empSal):
        self.empNo, self.empName, self.empDep, self.empSal = empNo, empName, empDep, empSal   
     
    def addNewEmployee(self):   
        Employee.employeeList.append(self)
    
    def getEmpList(self):
        return Employee.employeeList
    
    def getEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                return emp
        return False
    
    def updateEmpById(self,empNo, empName, empDep, empSal):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                emp.empNo, emp.empName, emp.empDep, emp.empSal = empNo, empName, empDep, empSal   
                return True
        return False
    
    def removeEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
              Employee.employeeList.remove(emp)
              return True
        return False
     
    
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
while choice >= 1 and choice <= 5:
    print("\n\n1. Add New Employee\n2. Get all Employee List\n3. Get Employee ID number\n4. Update Employee By ID\n5. Remove Employee By ID  \n\n")
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
            
    elif(choice == 3):
        empNo = int(input("Enter Employee Id:  "))
        emp = employee.getEmpById(empNo)
        if(emp == False):
            print("\nSorry...! Employee not found for id: " , empNo)
        else:
            print(emp)
    elif(choice == 4):
        empNo = int(input("Enter Your Employee ID number: "))
        empName = input("Enter Employee Name: ")
        empDep = input("Enter Employee Department: ")
        empSal = float(input("Enter Employee Salary: "))
        emp = employee.updateEmpById(empNo, empName, empDep, empSal)
        if(emp == False):
            print("\nSorry..! Update Failed. Employee Not Found ID: ", empNo)
        else:
            print("SuccessFully Employee update Id: ", empNo)
    
    elif(choice == 5):
        empNo = int(input("Enter Employee Id:  "))
        emp = employee.removeEmpById(empNo)
        if(emp == False):
            print("\nDelete! Employee not found for id: " , empNo)
        else:
            print("SuccessFully Removed Id: ", empNo)
        
        
    # try except block 
    # open data accepted file 
    #call that file with json file

    
<<<<<<< HEAD
=======
    
>>>>>>> 1c31f22cbea733d1878d770e8ddab58788ed71cb

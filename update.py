import os.path

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
    
    def removeEmpByID(self, empNo):
        Employee.employeeList = [emp for emp in self.employeeList if emp.empNo != empNo]
        return True
       
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
file_exists = os.path.exists('database.txt')
if file_exists == False:
    f = open("database.txt", "x")
else:
    print("File exists")
f = open("database.txt", "a")

while choice >= 1 and choice <= 5:
    print("\n\n1. Add New Employee\n2. Get all Employee List\n3. Get Employee ID number\n4. Update Employee By ID \n5. Remove Employee by ID\n\n")
    choice = int(input("Enter your Choice: "))
    if(choice == 1 ):
        while True:
            try:
                empNo = int(input("Enter Your Employee ID number: "))
                break
            except ValueError:
                print("Please enter an ID")
         
        empName = input("Enter Employee Name: ")
        empDep = input("Enter Employee Department: ")
        while True:
            try:
                empSal = float(input("Enter Employee Salary: "))
                break
            except ValueError:
                print(" please enter a valid Salary")
        emp = Employee(empNo, empName, empDep, empSal)
        emp.addNewEmployee()
        f.writelines(f"{(empNo)}\n")
        f.writelines(f"{str(empName)}\n")
        f.writelines(f"{str(empDep)}\n")
        f.writelines(f"{(empSal)}\n")
        f.writelines("====================")
        f.writelines("\n")
        
    elif(choice == 2 ):
        print("\n")
        for emp in employee.getEmpList():
            print(emp)
            
    elif(choice == 3):
        while True:
            try:
                empNo = int(input("Enter Employee Id:  "))
                break
            except ValueError:
                print("please enter a valid ID ")
        emp = employee.getEmpById(empNo)
        if(emp == False):
            print("\nSorry...! Employee not found for id: " , empNo)
        else:
            print(emp)
    elif(choice == 4):
        while True:
            try:
                empNo = int(input("Enter Your Employee ID number: "))
                break
            except ValueError:
                print("please enter a valid Id")
        empName = input("Enter Employee Name: ")
        empDep = input("Enter Employee Department: ")
        while True:
            try:
                empSal = float(input("Enter Employee Salary: "))
                break
            except ValueError:
                print("please enter a valid salary")
        emp = employee.updateEmpById(empNo, empName, empDep, empSal)
        if(emp == False):
            print("\nSorry..! Update Failed. Employee Not Found ID: ", empNo)
        else:
            print("SuccessFully Employee update Id: ", empNo)
    elif(choice == 5):
        empID = int(input("enter an employee Id to remove:"))
        employee.removeEmpByID(empID)
        
        
        # if has file == 
        

            
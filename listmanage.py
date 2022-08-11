import os
import platform

global listStd 
listStd = ["riyaz", "kishore", "pughal", "pavithra"]

def mangaeemployee(): 
	
	global bye 
	bye = "\n GOOD BYE" 

	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Employee Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Employee's List 
Enter 2 : To Add New Employee 
Enter 3 : To Search Employee 
Enter 4 : To Remove Employee 
		
		""")

	try: 
		userInput = int(input("Please Select An Above Option: "))
	except ValueError:
		exit("\nHy! That's Not A Number") 
	else:
		print("\n")

		
	if(userInput == 1): 
		print("List Employee's\n")  
		for employee in listStd:
			print("=> {}".format(employee))

	elif(userInput == 2): 
		newStd = input("Enter New Employee: ")
		if(newStd in listStd): 
			print("\nThis Employee {} Already In The Database".format(newStd))  
		else:	
			listStd.append(newStd)
			print("\n=> New Employee {} Successfully Add \n".format(newStd))
			for employee in listStd:
				print("=> {}".format(employee))	

	elif(userInput == 3):
		srcStd = input("Enter Employee Name To Search: ")
		if(srcStd in listStd): 
			print("\n=> Record Found Of Employee {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Employee {}".format(srcStd)) 

	elif(userInput == 4): 
		rmStd = input("Enter Employee Name To Remove: ")
		if(rmStd in listStd): 
			listStd.remove(rmStd)
			print("\n=> Employee {} Successfully Deleted \n".format(rmStd))
			for employee in listStd:
				print("=> {}".format(employee))
		else:
			print("\n=> No Record Found of This Employee {}".format(rmStd)) 
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")		
						
mangaeemployee()

def runAgain(): 
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		mangaeemployee()
		runAgain()
	else:
		quit(bye) 

runAgain()		

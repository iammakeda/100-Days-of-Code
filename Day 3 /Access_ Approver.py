#INPUT department name 
department_name = input("Enter Department Name: \n")
#INPUT system requested
system_request = input("What system is being requested? Payroll, CRM, or Admin_Console : \n")
#Yes or No for Manager approval 
manager_approval = input("Has this been approved by a manager? Yes or No: \n")
# Yes or No is security training complete 
security_training = input("Is security training complete? Yes or No:  \n")

print(f"Department: {department_name}")
print(f"System requested: {system_request}")
print(f"Manager approval? : {manager_approval}")
print(f"Training Complete?: {security_training}")

#Approval starts off as True and any flagged checks will change its value to False
approval = True
#.lower() method added to make everything lower case, so it's easier to match /compare
#All system requests require manager approval. It is an automatic denial if the answer is no
if manager_approval.lower() != "yes":
    print("DENIED : All system requests need manager approval before access is granted.")
    approval = False
else:
    #If manager approved, security training still needs to be completed for each system request. If not, ticket is escalated
    if security_training.lower() != "yes":
        print("ESCALATED: You must complete the training. Your request has been escalated to Security.")
        approval = False
    #Training is required for all systems, so system checks only run once training is complete 
    else: 
        #System checks only run if security training is confirmed completed
        # If the system request is admin_console , print line executes
        if system_request.lower() == "admin_console":
            print("Admin Console request processed!")
        # ELSE IF the system request says crm, the print line executes
        elif system_request.lower() == "crm":
            print("CRM request processed!")
        #ELSE IF the user requests payroll access, if they did not input finance or hr as their department, auto-Denial 
        elif system_request.lower() == "payroll": 
            if department_name.lower() != "finance" and department_name.lower() != "hr":
                print("DENIED: Payroll access islimited to Finance or HR department")
                approval = False 
            else:
                print("Payroll request processed!")
                
        #catch for any system request that does not match  crm, payroll and admin_console 
        else:
            print(f"{system_request} does not exist. Please try again.")
            approval = False
if approval:
    print("ACCESS APPROVED: Please check your email for the next steps.")

    #flag maybe ?
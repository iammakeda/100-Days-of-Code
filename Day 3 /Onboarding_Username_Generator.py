#Ask for first name, last name, worker type (employee of contractor) and contract length in months (contractors only)
#Build username as first intial plus the last name , allin lowercase. Contractors get a "c-" prefix
#Contractors on contracts longer than 12 months > print warning that HR needs to re-approve contract
#print summart with an f-string

#INPUT first name  and last name 
first_name = input("First name:")
last_name = input("Last name:")

#INPUT worker type  - employee or contractor
worker_type = input("Worker type:")


#username is the first letter of first name and last name 


#flag for hr contract approval
needs_hr_approval = False
#Flag for valid worker type 
valid_worker_type = True
#IF worker type is contractor with lower case 
if worker_type.lower() == "contractor":
    #IF the worker type is a contractor, the user name should be prefixed with a c-
    user_name = "c-" + first_name[0] + last_name 
    #INPUT contract length , convert data type to integer
    contract_length = int(input("Contract length (months): "))
    if contract_length > 12:
        #IF the contract length is greater than 12 , the flag is True
        needs_hr_approval= True        
#ELIF worker type is employee, the username is created by the first character of first name and whole last name
elif worker_type.lower() == "employee":
    #username is the first letter of first name and last name
    user_name = first_name[0] + last_name
    
else:
    print("Worker type unrecognized. Please try again")
    valid_worker_type= False
if valid_worker_type:
    print(f"--- Onboarding Summary ---\nUsername: {user_name.lower()} \nType: {worker_type}")
    if needs_hr_approval:
        print("Contract exceeds 12 months, so HR re-approval is required")

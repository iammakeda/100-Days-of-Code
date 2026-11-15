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

#print("First Name: " ,first_name)
#print("Last name: ", last_name)
#print("Worker type: ", worker_type)
#print("Contract length (months): ")



#IF worker type is contractor with lower case 
if worker_type.lower() == "contractor":
    #IF the worker type is a contractor, the user name should be prefixed with a c-
    user_name = "c-" + first_name[0] + last_name 
    #flag for hr contract approval
    needs_hr_approval = False
    #INPUT contract length , convert data type to integer
    contract_length = int(input("Contract length (months): "))
    if contract_length > 12:
        #IF the contract length is less than or equal to 12 , the flag is false
        needs_hr_approval= True
        print("Contract exceeds 12 months, so HR re-approval is required.")
#ELIF worker type is employee, the username is created by the first character of first name and whole last name
elif worker_type.lower() == "employee":
    user_name = first_name[0] + last_name      
else:
    if worker_type.lower() != "employee" and worker_type.lower() != "contractor":
        print("Work type unrecognized. Please try again")


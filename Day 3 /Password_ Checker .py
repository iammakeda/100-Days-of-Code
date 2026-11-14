#INPUT username
username = input("Create a username : \n")
#INPUT password 
password = input("Enter a password. NOTE: All passwords must be a minimum of 12 characters, at least one upper case letter and a special character from !, @, # or $ : \n")
#variable created to hold value of password length
num_of_pw_char = len(password)

#FLAG for each password requirement 
password_ok = True
#IF the character count is less than 12
if num_of_pw_char < 12:
    print(f"Your password is too short. The minimum is 12 characters and you currently have {num_of_pw_char}.")
    password_ok = False
#IF password has at least one uppercase letter , using .lower() method and compare
if password == password.lower():
    print("Your password needs at least one uppercase letter.")
    password_ok = False 
#IF check using AND logical operator. COUNT method needs to be greater than zero for any of the special characters
if password.count("!") + password.count("@") + password.count("#") + password.count("$") < 1:   
        print("Your password needs at least one special character (! @ # $)")
        password_ok = False 
#IF username is part of password
#LOWERCASE username and password to remove any uppercase characters that would prevent script from catching username match in password
lowercase_user = username.lower()
lowercase_pw = password.lower()
if lowercase_pw.count(lowercase_user) >= 1:
    print("You cannot include your username in your password.")
    password_ok = False 

if password_ok :
    print(f"Username: {username} \nPassword accepted!")  
        
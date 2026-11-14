#account types standard, admin,  or service 
account_type= input("Enter the account type (standard, admin or service) : \n")
#Request how many days since last login , change data type  from str to int
last_login_days = int(input("How many days since their last login?: \n"))
#Divide number of days by 7 without remainder 
week_count= int(last_login_days // 7)
#Calculate remainder  with modulo to add the day count
day_count = last_login_days % 7
print(f"Account type:{account_type}")
print(f"Days since last login: {last_login_days}")

week_word = ""
day_word = ""

#IF last login was a day ago 
#if last_login_days == 1:
    #print("Inactive for 1 day")
#IF last login is less than 7 days
#elif last_login_days < 7:
    #print(f"Inactive for {last_login_days} days")
#IF last login is exact 7 days 
#elif last_login_days == 7 :
    #print(f"Inactive for {week_count} week")
# conditional flow for using week/weeks and day/days
if week_count == 1:
    week_word = "week" 
else:
    week_word = "weeks"
if day_count == 1:
    day_word = "day"
else:
    day_word = "days"

#conditional flow for zeroed out weeks and days

if week_count < 1:
    print(f"Inactive for {day_count} {day_word}")
elif day_count < 1:
    print(f"Inactive for {week_count} {week_word}")
else:
    print(f"Inactive for {week_count} {week_word} and {day_count} {day_word}")
#elif week_count > 1 and day_count == 1:
# print(f"Inactive for {week_count} weeks and {day_count} day")
#elif week_count == 1 and day_count == 1 :
# print(f"Inactive for {week_count} week and {day_count} day")
#else:
    #print(f"Inactive for {week_count} weeks and {day_count} days")

active = True
#IF admin inactive more than 30 days DISABLE 
if account_type.lower() == "admin": 
    if last_login_days > 30:
        print("DISABLE: Admin accounts must be disabled after 30 Days of inactivity.")
        active = False
elif account_type.lower() == "standard":
    #IF last login days greater than 60 and up to/including 90 days WARN
    if last_login_days > 60 and last_login_days <= 90 :
        print("WARNING: This user is close to account policy limit for inactivity. User has been sent an email.")
        #Technically in good standing but do not want to encourage procrastination with fixing the issue
        active = False
    # ELIF last login more than 90 days DISABLE
    elif last_login_days > 90:
        print("DISABLE: Standard accounts must be disabled after 90 days of inactivity.")
        active= False
# ELIF account type is service and last login is more than 180 days 
elif account_type.lower() == "service":
    if last_login_days > 180:
        print("FLAGGED: This account has been flagged for owner review.")
        active = False
else: 
    print("This account type does not exist.")
    active = False
if active :
    print("This account is in good standing for now.")


# last login  more than 180, FLAG for owner review 
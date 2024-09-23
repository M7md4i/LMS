import time
import os

SystemDatabase = {}
SystemDatabase["m"] = {
                "Password" : "12345",
                "currently_logged_in" : False,
                "courses" : {
                }
            }


def run_the_system():
    print("Learning management System !")
    time.sleep(1) 
    while True:
        os.system('cls')
        get_number_of_users()
        print("- - - - - - - LMS(Main) - - - - - - -\n\n",
              ">> Welcome To Learning management System! The best system ever :D\n",
               "[1]: Register a new account\n",
               "[2]: Login on your account\n",
               "[3]: Exit\n",
               "- - - - - - - - - - - - - - - - - - - -"
              )
        Index = input("> Choose an option: ")  
        os.system('cls')
        if Index == '1' :
            registor_new_user()
        elif Index == '2':
            login()
        elif Index == '3':
            break
        else :
            print("Wrong index try again")
            time.sleep(1)
            os.system('cls')



def registor_new_user():
    get_number_of_users()
    print("- - - - - - - LMS(Registration) - - - - - - -\n")
    UserName = input("Enter User Name: ")
    Password = input("Enter Password: ")
    UserNameCheck = False
    PasswordCheck = False
    os.system('cls')
    while True:
        os.system('cls')
        get_number_of_users()
        print("- - - - - - - LMS(Registration) - - - - - - -\n")
        print("UserName: [",UserName.lower(),"]","\nPassword: [",Password,"]")  
        
        UserNameCheck = check_username(UserName)
        PasswordCheck = check_password(Password , UserName)
        if UserNameCheck and PasswordCheck :
            print("\nAll Your Inforamtion is Right You can create your Account\n",
                          "[C] For Create Account\n",
                          "[U] for Change UserName\n",
                          "[P] for Change Password\n",
                          "[E] for Exit\n")
        else :
            print("\nSorry some of your information is wrong read notion\n",
                          "[U] for Change UserName\n",
                          "[P] for Change Password\n",
                          "[E] for Exit\n")
        Index = input("> Choose an option: ")
        os.system('cls')
        get_number_of_users()
        print("- - - - - - - LMS(Registration) - - - - - - -\n")
        if Index == 'U' or Index == 'u':
            UserName = input("Enter User Name: ")
        elif Index == 'P' or Index == 'p' :
            Password = input("Enter Password: ")
        elif (Index == 'c' or Index == 'C') and UserNameCheck and PasswordCheck :
            os.system('cls')
            SystemDatabase[UserName] = {
                "Password" : Password,
                "currently_logged_in" : False,
                "courses" : {
                }
            }
            print("Your account was created")
            time.sleep(1)
            os.system('cls')
            break
        elif (Index == 'E') or (Index == "e"):
            break
        else:
            print("Wrong index try again")
            time.sleep(1)
        Index = 'x'
        os.system('cls')
        
def check_username(UserName):
    if UserName in SystemDatabase:
        print("     - The Username was taken try another user")
        return False
    else:
        return True
def check_password(Password , UserName):
    returnValue = True
    
    if len(Password) < 16 :
        print("     - The password must be 16 char or more")
        returnValue = False
    SpChar = "~`!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    NumOfSpChar = 0
    NumOfNumChar = 0

    for Char in Password:
        if Char.isdigit():
            NumOfNumChar += 1
        elif Char in SpChar:
            NumOfSpChar += 1
    
    if UserName in Password:
        print("     - The password must not contain the username")
        returnValue = False


    if NumOfNumChar < 2 and NumOfSpChar < 2:
        print("     - The password must contain 2 special char and 2 number")
        returnValue = False
    return returnValue

def login():
    get_number_of_users()
    print("- - - - - - - LMS(Login) - - - - - - -\n")
    UserName = input("Enter Your User Name: ")
    Password = input("Enter Your Password: ")
    x = '0'
    while True:
        os.system('cls')
        if (UserName in SystemDatabase) and SystemDatabase[UserName]["Password"] == Password :
            if(x == '0'):
                os.system('cls')
                print("welcome",UserName,"!")
                time.sleep(2)
                x = '1'
            os.system('cls')
            SystemDatabase[UserName]["currently_logged_in"] = True
            get_number_of_users()
            print("- - - - - - - LMS(Student Page) - - - - - - -\n",
               "[1]: Register a new course\n",
               "[2]: Retrieve Register courses\n",
               "[3]: Student information\n",
               "[4]: delete your accout\n",
               "[5]: Exit\n",
               "- - - - - - - - - - - - - - - - - - - -"
              )
            Index = input("> Choose an option: ")  
            if(Index == '1'):
                add_new_courses(UserName)
            if(Index == '2'):
                Retrieve_Register_courses(UserName)
            if(Index == '3'):
               see_user_info(UserName)
            if(Index == '4'):
                remove_my_acc(UserName)
                break
            if(Index == '5'):
                SystemDatabase[UserName]["currently_logged_in"] = False
                break
        else:
            os.system('cls')
            print("wrong password or Username")
            time.sleep(2)
            break


def get_number_of_users():
    count = 0

    for user in SystemDatabase:
        if SystemDatabase[user]["currently_logged_in"]:
            count += 1
    print("number of user in system [",count,"]\n\n")



def add_new_courses(UserName):
    os.system('cls')
    tep = ''
    while(tep != 'e'):
        Coures_name = input("Enter coures name : ")
        Coures_GPA = 0
        while(True):
            Coures_GPA =  int(input("Enter GPA : "))
            if Coures_GPA < 0 or Coures_GPA > 100:
                print("the gpa must be in range 0 - 100")
            else:
                break
        SystemDatabase[UserName]["courses"][Coures_name] = Coures_GPA
        tep = input("do you want Register other course? press enter or type 'e' to exit: ")
        os.system('cls')

def Retrieve_Register_courses(UserName):
    os.system('cls')
    print("your Register courses : ")
    for course, gpa in SystemDatabase[UserName]["courses"].items():
        print("Course: ",course, "     GPA:", gpa)
    input("press enter to back :")

def see_user_info(UserName):
    AGpa = 0
    numcourse = 0
    for course,gpa in SystemDatabase[UserName]["courses"].items():
        AGpa =  AGpa + gpa
        numcourse = numcourse + 1        
    print("Name : ",UserName,
          "\nnumber of courses :" ,numcourse,
          "\nGPA : ", AGpa/numcourse)
    input("press enter to back :")

def remove_my_acc(UserName):

    Pass = input("please Enter Your Password: ")
    if SystemDatabase[UserName]["Password"] == Pass :
        temp = input("Are you sure ? [Y/N] : ")
        if temp == 'Y' or temp == 'y':
            del SystemDatabase[UserName]
            print("your accout successfully deleted")
            time.sleep(2)
            os.system('cls')
        else : 
            print("deleted account was cancelled.")
            time.sleep(2)
            os.system('cls')

os.system('cls')
run_the_system()
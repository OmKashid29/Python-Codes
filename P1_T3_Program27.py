# Login system using username and password.

def Login(Username,Password,Username1,Password1):
    if (Username != Username1):
        print("Please enter valid username ")

    elif (Password !=Password1):
        print("Please enter valid password ")

    else:
        print("Login successfully")

def main():
    Username = "omkashid"
    Password = "osk@2006"

    Username1 = input("Enter the username : ")
    Password1 = input("Enter the password : ")

    Login(Username,Password,Username1,Password1)

if __name__=="__main__":
    main()
def all():
    '''
    This function holds all data methods
    '''
    print("log-for old user","new-new user","newc-new credentials","viewc-view credentials")
    calls = input("call: ")
    if calls == "new":
        user.add_user()
        all()
    elif calls == "log":
        login()
        cred.create_credentials()
    elif calls == "viewc":
        login()
        cred.show_credentials()

def login():
    print('Logging in')
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    for line in open("mastcred.txt","r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("correct creds")
            inline_codes()
            return True

    print("incorrect")

    return False

def inline_codes():
    '''
    Function that allows one to navigate users menu
    '''
    print("Calls\n ncred-create credentials")
    inline_calls = input("inline call: ")
    if inline_calls == "ncred":
        cred.create_credentials()


class User:
    """
    Class that generates new instances of users

    """

    def add_user(self):
        print('Creating user, please choose username and password')
        username = input('Username: ')
        password = input('Password: ')

        file = open("mastcred.txt","a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()


class Credentials:
    """
    Class that generates new instances of credentials

    """
    def create_credentials(self):
    print("confirm your username")
    name = input("username: ")
    file = open("mastcred.txt", "r")
    for line in file.readlines():
        login_info = line.split()
        if (name in login_info):
            print("you can now create your credentials")
            print("Please enter the credentials of your choice")
            account = input('Account: ')
            accntpassword = input('A/c Password: ')
            file = open(f"{name}.txt","a")
            file.write(account)
            file.write(" ")
            file.write(accntpassword)
            file.write("\n")
            file.close()

    def view_credentials(self):
        print("confirm usernmae to view credntials")
        name = input("username: ")
        file = open("mastcred.txt", "r")
        for line in file.readlines():
            login_info = line.split()
            if (name in login_info):
                print("Success")
                nfile = open(f"{name}.txt","r")
                for line in nfile.readlines():
                    userinfo = line.split()
                    for entry in userinfo:
                        print(entry)
                return True
        print("access denied")
        return False

    def pass_gen(self):

        import secrets
        import string
        print("confirm username to generate password")
        name = input("username: ")
        file = open("mastcred.txt", "r")
        for line in file.readlines():
            login_info = line.split()
            if (name in login_info):
                print("Success")
                print("Enter account to be assigned passkey")
                account = input('Account: ')
                alphabet = string.ascii_letters + string.digits
                accntpassword = ''.join(secrets.choice(alphabet) for i in range(20))
                file = open(f"{name}.txt","a")
                file.write(account)
                file.write(" ")
                file.write(accntpassword)
                file.write("\n")
                file.close()
                return True
        print("access denied")
        return False

    def pass_copy(self):

        import pyperclip
        print("confirm username to copy password")
        name = input("username: ")
        file = open("mastcred.txt", "r")
        for line in file.readlines():
            login_info = line.split()
            if (name in login_info):
                print("Success")
                print("Input name of account you want password copied")
                account = input("Account: ")
                cfile = open(f"{name}.txt","r")
                for line in cfile.readlines():
                    infocopy = line.split()
                    if (account in infocopy):

                        infocopy = line.split()
                        pyperclip.copy(infocopy)
                        print("success")
                        return(infocopy)
                    return True
        print("access denied")
        return False


all()

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
        cred.show_credentials()\

def login():
    print('Logging in')
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    for line in open("mastcred.txt","r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("correct creds")
            return True

    print("incorrect")

    return False


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
all()

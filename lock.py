def all():
    '''
    This function holds all data methods
    '''

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

import unittest
from lock import User
from lock import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_add_user(self):
        '''
        Tests if the user has been added
        '''
        line = "user password"
        self.assertEqual(line,User.add_user(self))

if __name__ == '__main__':
    unittest.main()

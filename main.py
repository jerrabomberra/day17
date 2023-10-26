"""class about classes"""
class User:
    def __init__(self, user_id, user_name):
        """initialises attributes"""
        self.user_id=user_id
        self.user_name=user_name


    def printit(self, user_id, user_name):
        """prints something out"""
        print(f"Your user id is {user_id}, and your user name is {user_name}")


user_1=User("001","Doug")
user_1.printit('001','Doug')


user_2=User("002","Bob")
user_2.printit('002','Bob')

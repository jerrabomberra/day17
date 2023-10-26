"""class about classes"""
class User:
    def __init__(self, user_id, user_name):
        """initialises attributes"""
        self.user_id=user_id
        self.user_name=user_name
        self.followers = 3

    def printit(self, user_id, user_name):
        """prints something out"""
        print(f"Your user id is {user_id}, your user name is {user_name} \
and you have {self.followers} followers.")


user_1=User("001","Doug")
user_1.followers +=6
user_1.printit('001','Doug')
# print(user_1.followers)

# user_2=User("002","Bob")
# user_2.printit('002','Bob')

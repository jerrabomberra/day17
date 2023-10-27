"""class about classes"""

class User:
    """ this is a class"""
    def __init__(self, user_id, user_name):
        """initializes attributes"""
        self.user_id=user_id
        self.user_name=user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """ determines the number of followers and followings"""
        user.followers += 1
        self.following += 1



user_1 = User("001","Doug")
user_2 = User("002","Jill")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# print(user_1.followers)

# user_2=User("002","Bob")
# user_2.printed('002','Bob')

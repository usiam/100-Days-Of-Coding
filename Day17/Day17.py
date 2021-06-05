
# =============================================================================
# Day 17: Creating a OOP program
# =============================================================================

# 152, 153, 154. Creating a class, constructor, and methods

class User: # class name is always PascalCase
    pass # just passes the line of code
# using a constructor to initialize the object
    def __init__(self, id, username): # called EVERY TIME a new User object is created
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User(0, 'Jack')
user2 = User(1, 'Dingus')

user1.follow(user2)
print(user1.followers, user1.following, user2.followers, user2.following)


# =============================================================================
# End of Day 17
# =============================================================================
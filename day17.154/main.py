class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # the user we are following, their follower count goes up by one.
        user.followers += 1
        self.following += 1


user_1 = User("001", "Rene")
user_2 = User("002", "Nicole")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"


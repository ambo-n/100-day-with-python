class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower =0

user_1 = User("001", username="Angela")
user_1.id = "001"
# user_1.username = "me"
print(user_1.username)
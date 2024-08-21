import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.username = name
        self.followers = 0
        self.following = 0

    def introduce(self):
        print(f"Hey, my name is {self.username}.\nI am following {
              self.following} and I have {self.followers} followers.")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Anna")
user2 = User("Jerry")

user1.follow(user2)
user1.introduce()
user2.introduce()

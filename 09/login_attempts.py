class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.user_info)

    def greet_user(self):
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User('yi', 'pan', location='birmingham', company='university of birmingham')
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)

class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.user_info)

    def greet_user(self):
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}")
        
user1 = User('yi', 'pan', location='birmingham', company='university of birmingham')
user2 = User('lin', 'Wang', location='birmingham', company='ukpathway')
user3 = User('yuang', 'Pan', location='hangzhou')

user1.describe_user()
user1.greet_user()

print("\n")

user2.describe_user()
user2.greet_user()

print("\n")

user3.describe_user()
user3.greet_user()

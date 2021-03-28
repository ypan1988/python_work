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

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

# user1 = Admin('yi', 'pan', location='birmingham', company='university of birmingham')
# user1.privileges.show_privileges()

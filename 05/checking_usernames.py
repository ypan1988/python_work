current_users = ['User1', 'user2', 'admin', 'user4', 'User5']
new_users = ['user5', 'user7', 'user8', 'user9', 'user10']

current_users_copy = [user.lower() for user in current_users]

for user in new_users:
    if user in current_users_copy:
        print("Please enter a new username")
    else:
        print("The username is available")

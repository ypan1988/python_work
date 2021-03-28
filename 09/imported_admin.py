from privileges import Admin

user1 = Admin('yi', 'pan', location='birmingham', company='university of birmingham')
user1.privileges.show_privileges()

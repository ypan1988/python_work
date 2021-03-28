person_0 = {
    'first_name': 'yi',
    'last_name': 'pan',
    'age': 32,
    'city': 'birmingham'
}

person_1 = {
    'first_name': 'lin',
    'last_name': 'wang',
    'age': 32,
    'city': 'birmingham'
}

person_2 = {
    'first_name': 'yuang',
    'last_name': 'pan',
    'age': 2,
    'city': 'hangzhou'
}

people = {
    'person_0': person_0,
    'person_1': person_1,
    'person_2': person_2
}

for username, user_info in people.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    age = user_info['age']
    location = user_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tLocation: {location.title()}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


names = ['yi', 'jen', 'sarah', 'lin', 'edward', 'phil', 'yuang']

for name in names:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")

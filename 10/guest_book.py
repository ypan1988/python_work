filename = 'guest_book.txt'

while True:
    guest_name = input("Please input your name (Enter 'q' to quit): ")
    if guest_name == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"{guest_name}\n")

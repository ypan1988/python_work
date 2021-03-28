with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

print("-----")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

print("-----")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("-----")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

names = ['yi pan', 'lin wang', 'yuang pan']
print(f"Hi, {names[0].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[1].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[2].title()}. Are you available for the dinner tonight?")
print(f"{names[2].title()} is not available for the dinner tonight!")

names[2] = 'jianwen fu'
print(f"Hi, {names[0].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[1].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[2].title()}. Are you available for the dinner tonight?")

print("Hi, all. I just found a bigger table, so now more space is available.")
names.insert(0, 'hanming pan')
names.insert(2, 'fengmei pan')
names.append('shuijuan pan')
print(f"Hi, {names[0].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[1].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[2].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[3].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[4].title()}. Are you available for the dinner tonight?")
print(f"Hi, {names[5].title()}. Are you available for the dinner tonight?")
print("Sorry, guys. I can only invite two people for dinner.")

print(names)
poped_name = names.pop()
print(f"Sorry, {poped_name.title()}. I can't invite you to dinner.")
poped_name = names.pop()
print(f"Sorry, {poped_name.title()}. I can't invite you to dinner.")
poped_name = names.pop()
print(f"Sorry, {poped_name.title()}. I can't invite you to dinner.")
poped_name = names.pop()
print(f"Sorry, {poped_name.title()}. I can't invite you to dinner.")
print(names)

del names[0]
print(names)
del names[0]
print(names)

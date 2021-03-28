pizzas = ['pepperoni', 'cheeseburger', 'bbq']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('hawaiian')
friend_pizzas.append('hot & spicy')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza}")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"{pizza}")

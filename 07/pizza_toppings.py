prompt = "What do you want for pizza topping?"
prompt += "\n(Enter 'quit' when you are finished.) "

topping = ""
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.")

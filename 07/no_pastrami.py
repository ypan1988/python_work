print("The deli has run out of pastrami\n")

sandwich_orders = ['tuna sandwich', 'pastrami', 'chicken sandwich', 'pastrami', 'duck sandwich', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)

print("\nAll finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich}")

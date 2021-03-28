def make_sandwiches(*items):
    print("\nMaking a Sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwiches('chicken')
make_sandwiches('chicken', 'tomato')
make_sandwiches('chicken', 'tomato', 'lettuce')

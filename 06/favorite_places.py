favorite_places = {
    'yi': ['shanghai', 'london', 'hongkong'],
    'lin': ['hangzhou', 'singapore'],
    'yuang': ['hangzhou']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

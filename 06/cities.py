cities = {
    'shanghai': {
        'country': 'china',
        'population': 26320000,
        'fact': 'financial centre'
    },
    'london': {
        'country': 'uk',
        'population': 7451000,
        'fact': 'financial centre'
    },
    'hongkong': {
        'country': 'china',
        'population': 8982000,
        'fact': 'financial centre'
    }
}

for city, city_info in cities.items():
    print(f"\ncity      : {city.title()}")
    print(f"country   : {city_info['country'].title()}")
    print(f"population: {city_info['population']}")
    print(f"fact      : {city_info['fact'].title()}")

rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in set(rivers.values()):
    print(country.title())

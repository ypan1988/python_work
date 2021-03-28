pet_0 = {
    'species': 'dog',
    'owner': 'yi'
}

pet_1 = {
    'species': 'cat',
    'owner': 'lin'
}

pet_2 = {
    'species': 'bird',
    'owner': 'yuang'
}

pets = {
    'pet_0': pet_0,
    'pet_1': pet_1,
    'pet_2': pet_2
}

for key, value in pets.items():
    print(f"\nPet: {key}")
    print(f"\tSpecies: {value['species']}")
    print(f"\tOwner's Name: {value['owner']}")

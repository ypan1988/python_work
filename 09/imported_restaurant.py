from restaurant import Restaurant

restaurant = Restaurant('KFC', 'American')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('Burger & Lobster', 'British')
restaurant2 = Restaurant('Hanchao', 'Chinese')
restaurant3 = Restaurant('Tops', 'Chinese')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

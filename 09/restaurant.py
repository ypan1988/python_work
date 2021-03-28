class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open.")

# restaurant = Restaurant('KFC', 'American')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant1 = Restaurant('Burger & Lobster', 'British')
# restaurant2 = Restaurant('Hanchao', 'Chinese')
# restaurant3 = Restaurant('Tops', 'Chinese')

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

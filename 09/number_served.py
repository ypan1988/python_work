class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open.")

    def set_number_served(self, n_served):
        self.number_served = n_served

    def increment_number_served(self, n_incr):
        self.number_served += n_incr

        
restaurant = Restaurant('KFC', 'American')
print(restaurant.number_served)

restaurant.set_number_served(100)
print(restaurant.number_served)

restaurant.increment_number_served(50)
print(restaurant.number_served)

from models.restaurant import Restaurant


class RestaurantService:
    def __init__(self, restaurant_repository):
        self.restaurant_repository = restaurant_repository

    def create_restaurant(self, name, city):
        restaurant = Restaurant(name, city)
        self.restaurant_repository.save(restaurant)
        return restaurant

    def list_restaurants(self):
        return self.restaurant_repository.get_all()

    def get_restaurant(self, restaurant_id):
        return self.restaurant_repository.get_by_id(restaurant_id)
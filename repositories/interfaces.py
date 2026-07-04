from abc import ABC, abstractmethod

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def save(self, customer):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, customer_id):
        pass

class RestaurantRepositoryInterface(ABC):
    @abstractmethod
    def save(self, restaurant):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, restaurant_id):
        pass

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def get_all(self):
        pass
from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_charge(self, distance):
        pass

    @abstractmethod
    def get_type(self):
        pass


class BikeDelivery(DeliveryStrategy):
    def calculate_charge(self, distance):
        return 30 + distance * 5

    def get_type(self):
        return "BIKE"


class CarDelivery(DeliveryStrategy):
    def calculate_charge(self, distance):
        return 60 + distance * 8

    def get_type(self):
        return "CAR"  
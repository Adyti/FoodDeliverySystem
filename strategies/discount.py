from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, amount):
        return 0


class PremiumDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.10


class FestivalDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.20
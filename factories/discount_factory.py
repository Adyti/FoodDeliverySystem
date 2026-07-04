from strategies.discount import NoDiscount, PremiumDiscount, FestivalDiscount


class DiscountFactory:
    @staticmethod
    def create(discount_type):
        if discount_type == "premium":
            return PremiumDiscount()
        if discount_type == "festival":
            return FestivalDiscount()
        return NoDiscount()  
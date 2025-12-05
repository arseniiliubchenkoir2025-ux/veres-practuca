class Sneakers:

    def __init__(self, id , brand="", size=0, color="", price=0.0, quantity=0, material="", number_of_sales=0):
        self.id = id
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__price = price
        self.__quantity = quantity
        self.__material = material
        self.__number_of_sales = number_of_sales

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price <0")
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError("quantity <0")
        self.__quantity = quantity

    @property
    def number_of_sales(self):
        return self.__number_of_sales

    @number_of_sales.setter
    def number_of_sales(self, number_of_sales):
        if number_of_sales < 0:
            raise ValueError("sales can not be negative")
        self.__number_of_sales = number_of_sales

    def __str__(self):
        return f"{self.__brand} ({self.__color}), price: {self.__price}, qty: {self.__quantity}, sold: {self.__number_of_sales}"


class SportShoesStore:
    def __init__(self):
        self.sneakers = []

    def add_sneakers(self, sn):
        existing = [s for s in self.sneakers if s.brand.lower() == sn.brand.lower()]
        if existing:
            sn.id = existing[0].id
            existing[0].quantity += 1
        else:
            if self.sneakers:
                max_id = max(s.id for s in self.sneakers)
                sn.id = max_id + 1
            else:
                sn.id = 0
                sn.quantity = 1
            self.sneakers.append(sn)
    def sort_by_price(self):
        return sorted(self.sneakers, key=lambda x: x.price)

    def sort_by_quantity(self):
        return sorted(self.sneakers, key=lambda x: x.quantity)

    def get_top_popular(self, top=3):
        return sorted(self.sneakers, key=lambda x: x.number_of_sales, reverse=True)[:top]


def main():
    store = SportShoesStore()

    s1 = Sneakers(0, "Nike AirMax", 42, "white", 5600, 5, "leather", 120)
    s2 = Sneakers(1, "Adidas Yeezy", 43, "black", 8200, 3, "mesh", 200)
    s3 = Sneakers(2, "Puma RS-X", 42, "blue", 4700, 9, "synthetic", 80)
    s4 = Sneakers(2, "Puma RS-X", 42, "blue", 4700, 9, "synthetic", 80)
    store.add_sneakers(s1)
    store.add_sneakers(s2)
    store.add_sneakers(s3)
    store.add_sneakers(s4)
    print("sort by price:")
    for i in store.sort_by_price():
        print(i)

    print("\nsort by quantity:")
    for i in store.sort_by_quantity():
        print(i)

    print("\nTOP popular:")
    for i in store.get_top_popular():
        print(i)


main()

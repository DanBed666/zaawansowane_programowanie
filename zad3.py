class Property:

    def __init__(self, area, rooms, price, address):

        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Miejsce: {self.area}, Liczba pokoi: {self.rooms}, Cena: {self.price}, Adres: {self.address}"


class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}, Dzialka: {self.plot}"


class Flat(Property):

    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}, Piętro: {self.floor}"


if __name__ == '__main__':

    p = Property("Kato", 8, 2000, "Zielona 13")
    print(p.__str__())
    h = House("Gleiwitz", 5, 2500, "Pomidorowa 8", 50)
    print(h.__str__())
    f = Flat("Gdynia", 6, 8000, "Arki Noego 66", 13)
    print(f.__str__())


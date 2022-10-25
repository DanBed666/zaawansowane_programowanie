import magazine.utils as utils


class Product:

    def __init__(self):
        self.nazwa = utils.losowywyraz()
        self.czas_ladowania = utils.czas_ladowania()

    def __str__(self):
        return f"Nazwa produktu: {self.nazwa} i czas ładowania: {self.czas_ladowania}"
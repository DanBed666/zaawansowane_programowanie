import magazine.utils as utils


class Order:

    def __init__(self):
        self.czas_zamowienia = utils.czas_zamowienia()
        self.status = utils.status()

    def __str__(self):
        return f"Czas zamowienia: {self.czas_zamowienia} i status zamowienia: {self.status}"
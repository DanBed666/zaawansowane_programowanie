class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w mieście {self.city} na ulicy {self.street}, kod pocztowy {self.zip_code} otwarta przez {self.open_hours} godzin" \
               f", numer telefonu to {self.phone}"


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik biblioteki {self.first_name} {self.last_name} zatrudniony {self.hire_date} urodzony {self.birth_date} zamieszkały {self.city}" \
               f" na ulicy {self.street} z kodem pocztowym {self.zip_code}, a jego numer telefonu to {self.phone}"

class Book:

    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Ksiazka pochodzaca z biblioteki {self.library} opublikowana {self.publication_date}. " \
               f" Autorem tej ksiazki jest {self.author_name} {self.author_surname}." \
               f" Ksiazka ma {self.number_of_pages} stron"

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):

        return self.marks > 50

    def __str__(self):
        return f"Imie {self.name} z ocena z jakiegos tam testu {self.marks}"


class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Zamowienie dla pracownika {self.employee} od studenta {self.student}." \
               f" Liczba ksiazek {self.books}. Data zamowienia {self.order_date}"


if __name__ == '__main__':

    l1 = Library("Katowice", "Zielona", "66-420", 8, "666123909")
    l2 = Library("Zabrze", "Czerwona", "66-421", 9, "696180909")

    b1 = Book(l1, "16/05/2001", "Robert", "Lewandowski", 198)
    b2 = Book(l2, "17/05/2003", "Mirosław", "Klose", 168)
    b3 = Book(l2, "26/09/2004", "Jerzy", "Janowicz", 280)
    b4 = Book(l1, "08/08/2008", "Andrew", "Golota", 667)
    b5 = Book(l1, "01/01/2010", "Giancarlo", "Fisichella", 188)

    e1 = Employee("Piotr", "Protasiewicz", "12/08/2018", "12/06/1976", "Chorzow", "Czerwona", "66-420", "666789123")
    e2 = Employee("Bartosz", "Zmarzlik", "19/07/2019", "19/07/1983", "Zielona Gora", "Rozowa", "66-421", "606789123")
    e3 = Employee("Jaroslaw", "Hampel", "19/01/2018", "19/07/1985", "Bydgoszcz", "Ogorkowa", "66-422", "686789123")

    s1 = Student("Maciek", 76)
    s2 = Student("Grzechu", 56)
    s3 = Student("Stefan", 69)

    o1 = Order(e1, s1, b2, "13/10/2013")
    print(o1.__str__())
    o2 = Order(e2, s2, b3, "13/10/2013")
    print(o2.__str__())


class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w mieście {self.city} na ulicy {self.street}, " \
               f"kod pocztowy " \
               f"{self.zip_code} otwarta w godzinach {self.open_hours}" \
               f", numer telefonu to {self.phone}"


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik biblioteki {self.first_name} {self.last_name} " \
               f"zatrudniony {self.hire_date} " \
               f"urodzony {self.birth_date} zamieszkały {self.city}" \
               f" na ulicy {self.street} z kodem pocztowym {self.zip_code}," \
               f" a jego numer telefonu to {self.phone}"


class Book:

    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Ksiazka pochodzaca z biblioteki " \
               f"{self.library} opublikowana " \
               f"{self.publication_date}. " \
               f" Autorem tej ksiazki jest {self.author_name} " \
               f"{self.author_surname}." \
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
        return f"Zamowienie dla pracownika {self.employee} od " \
               f"studenta {self.student}." \
               f" Liczba ksiazek {self.books}. " \
               f"Data zamowienia {self.order_date}"


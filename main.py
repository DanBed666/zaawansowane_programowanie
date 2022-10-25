from zad1 import Student
from zad2 import Library, Book, Employee, Order
from zad3 import Property, House, Flat


if __name__ == '__main__':

    s1 = Student("Marcin", 25)
    print(s1.is_passed())
    s2 = Student("Krzychu", 76)
    print(s2.is_passed())

    l1 = Library("Katowice", "Zielona", "66-420", "8-19", "666123909")
    l2 = Library("Zabrze", "Czerwona", "66-421", "9-20", "696180909")

    b1 = Book(l1, "16/05/2001", "Robert", "Lewandowski", 198)
    b2 = Book(l2, "17/05/2003", "Mirosław", "Klose", 168)
    b3 = Book(l2, "26/09/2004", "Jerzy", "Janowicz", 280)
    b4 = Book(l1, "08/08/2008", "Andrew", "Golota", 667)
    b5 = Book(l1, "01/01/2010", "Giancarlo", "Fisichella", 188)

    e1 = Employee("Piotr", "Protasiewicz", "12/08/2018", "12/06/1976",
                  "Chorzow", "Czerwona", "66-420", "666789123")
    e2 = Employee("Bartosz", "Zmarzlik", "19/07/2019", "19/07/1983",
                  "Zielona Gora", "Rozowa", "66-421", "606789123")
    e3 = Employee("Jaroslaw", "Hampel", "19/01/2018", "19/07/1985",
                  "Bydgoszcz", "Ogorkowa", "66-422", "686789123")

    s1 = Student("Maciek", 76)
    s2 = Student("Grzechu", 56)
    s3 = Student("Stefan", 69)

    o1 = Order(e1, s1, b2, "13/10/2013")
    print(o1.__str__())
    o2 = Order(e2, s2, b3, "13/10/2013")
    print(o2.__str__())

    p = Property("Kato", 8, 2000, "Zielona 13")
    print(p.__str__())
    h = House("Gleiwitz", 5, 2500, "Pomidorowa 8", 50)
    print(h.__str__())
    f = Flat("Gdynia", 6, 8000, "Arki Noego 66", 13)
    print(f.__str__())

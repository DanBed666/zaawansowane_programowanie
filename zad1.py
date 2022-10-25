class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):

        return self.marks > 50


if __name__ == '__main__':

    s1 = Student("Marcin", 25)
    print(s1.is_passed())
    s2 = Student("Krzychu", 76)
    print(s2.is_passed())

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):

        return self.marks > 50


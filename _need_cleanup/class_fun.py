
import csv
class Person:

    def __init__(self):
        self.name = "Anshuma"
        self.age = "27"
        self.goo = 10

    def update_name(self, name):
        self.name = name

    def update_age(self, age):
        self.age = age

p = csv.DictWriter()
p.writeheader()

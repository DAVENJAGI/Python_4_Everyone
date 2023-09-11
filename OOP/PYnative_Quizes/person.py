from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if today < date(self.date_of_birth.day, self.date_of_birth.month, today.year):
            age -= 1
        return age

person1 = Person("Chris", "Kenya", "9-2-2002")

print(" person1.")
print("Name: ", person1.name)
print("Country: ", person1.country)
print("DOB: ", person1.date_of_birth)
print("Age: ", person1.calculate_age())

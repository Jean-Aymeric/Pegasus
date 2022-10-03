from Hotel import Hotel
from Person import Person
from Employee import Employee


myHotel = Hotel("Pegasus")
person1 = Person("Mme", "THRACE", "Kara")
person2 = Person("M.", "BALTAR", "Gaïus")
person3 = Employee("Mme", "ROSLIN", "Laura", "18 octobre 2004")
myHotel.hireEmployee(person3)
person1.visitHotel(myHotel, "2 décembre 2005", "17 décembre 2005")
person1.visitHotel(myHotel, "19 janvier 2007", "23 janvier 2007")
person2.visitHotel(myHotel, "24 janvier 2005", "25 janvier 2005")

from Person import Person


class Employee(Person):
    __hireDate: str

    def __init__(self, gender: str, firstname: str, lastname: str, hireDate: str):
        Person.__init__(self, gender, firstname, lastname)
        self.__hireDate = hireDate

    def getHireDate(self) -> str:
        return self.__hireDate
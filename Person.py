from Visit import Visit


class Person:
    __firstname: str
    __lastname: str
    __gender: str
    __visits: [Visit]

    def __init__(self, gender: str, firstname: str, lastname: str):
        self.__gender = gender
        self.__firstname = firstname
        self.__lastname = lastname
        self.__visits = []

    def getFirstname(self) -> str:
        return self.__firstname

    def getLastname(self) -> str:
        return self.__lastname

    def getGender(self) -> str:
        return self.__gender

    def visitHotel(self, hotel, startDate: str, endDate: str):
        newVisit = Visit(self, hotel)
        newVisit.setStartDate(startDate)
        newVisit.setEndDate(endDate)
        self.__visits.append(newVisit)

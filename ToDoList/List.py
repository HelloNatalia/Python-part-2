from datetime import datetime

class List():
    id: int = 0
    week = ['Poinedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

    def __init__(self, title, description, date, daytodo = None, day_of_week = None):
        List.id += 1
        self.__id = List.id
        self.__title = title
        self.__description = description
        self.__date = date
        self.__daytodo = daytodo
        self.__day_of_week = day_of_week
    
    @staticmethod
    def date() -> str:
        """Odczytuje datę od użytkownika i sprawdza jej poprawność"""
        day, month, year = "", "", ""
        while True:
            day = input("Wprowadź dzień w formacie DD: ")
            month = input("Wprowadź miesiąc w formacie MM: ")
            year = input("Wprowadź rok w formacie YYYY: ")
            if len(day) == 2 and len(month) == 2 and len(year) == 4 and (day+month+year).isdigit():
                if int(month) in (1,3,5,7,8,10,12):
                    if int(day) <= 31: break
                if int(month) == 2:
                    if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
                        if int(day) <= 29: break
                    else:
                        if int(day) <= 28: break
                elif int(month) <= 12:
                    if int(day) <= 30: break
        date = day+"-"+month+"-"+year
        return date
    
    @staticmethod
    def dayToDo(deadline) -> list:
        """Sprawdza czy użytkownik chce przypisać do konkretnego dnia zadanie i to robi, czy nie"""
        while True:
            yes_or_no = input("Czy chcesz przypisać to zadanie do konkretnego dnia? (t/n): ")
            if yes_or_no == 't':
                while True:
                    daytodo = List.date()
                    date_format = "%d-%m-%Y"
                    daytodo_obj = datetime.strptime(daytodo, date_format).date()
                    deadline_obj = datetime.strptime(deadline, date_format).date()
                    if daytodo_obj <= deadline_obj:
                        day_of_week = daytodo_obj.weekday()
                        daytodo = daytodo_obj.strftime(date_format)
                        break
                    else:
                        print("Wprowadzona przez ciebie data jest po terminie do wykonania.\n")
                return_list = [day_of_week, daytodo]
                break
            elif yes_or_no == 'n':
                return_list = [None, None]
                break
        return return_list
              
    @staticmethod
    def createTask() -> object:
        """Tworzy zadanie"""
        title = input("Wprowadź tytuł zadania: ")
        description = input("Wprowadź opis zadania: ")
        date = List.date()
        daytodo_info = List.dayToDo(date)
        daytodo = daytodo_info[1]
        day_of_week = daytodo_info[0]
        task = List(title, description, date, daytodo, day_of_week)
        return task

    def showTask(self) -> str:
        """Pokazuje podstawowe informacje o zadaniu"""
        # return f"\n{self.__id} - {self.__title} - {self.__date}"
        if self.__daytodo and self.__day_of_week:
            return f"\n{self.__id} - {self.__title} - {self.__date}\nDo wykonania w: {List.week[self.__day_of_week]} {self.__daytodo}"
        else:
            return f"\n{self.__id} - {self.__title} - {self.__date}"
    
    def getId(self) -> int:
        """Pobiera id zadania"""
        return self.__id
    def getTitle(self) -> str:
        """Pobiera tytuł zadania"""
        return self.__title
    def getDescription(self) -> str:
        """Pobiera opis zadania"""
        return self.__description
    def getDate(self) -> str:
        """Pobiera datę"""
        return self.__date
    def getDaytodo(self) -> str:
        """Pobiera datę, do której jest przypisane zadanie"""
        return self.__daytodo
    def getDay_of_week(self) -> int:
        """Pobiera numer odpowiadający konkretnemu dniu tygodnia (0 - Poniedziałek, 1 - Wtorek, ...)"""
        return self.__day_of_week
    
    def changeTitle(self, new_title) -> None:
        """Zmienia tytuł"""
        self.__title = new_title
    def changeDescription(self, new_desc) -> None:
        """Zmienia opis"""
        self.__description = new_desc
    def changeDate(self, new_date) -> None:
        """Zmienia datę"""
        self.__date = new_date
    def changeDaytodo(self, new_daytodo, new_day_of_week) -> None:
        """Zmienia datę, do której przypisane jest zadanie i odpowiadający jej dzień tygodnia"""
        self.__daytodo = new_daytodo
        self.__day_of_week = new_day_of_week
    
    
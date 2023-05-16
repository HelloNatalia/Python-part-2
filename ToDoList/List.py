class List():
    id: int = 0

    def __init__(self, title, description, date):
        List.id += 1
        self.__id = List.id
        self.__title = title
        self.__description = description
        self.__date = date
    
    @staticmethod
    def date():
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
    def createTask():
        title = input("Wprowadź tytuł zadania: ")
        description = input("Wprowadź opis zadania: ")
        date = List.date()
        task = List(title, description, date)
        return task

    def showTask(self):
        return f"\n{self.__id} - {self.__title} - {self.__date}"
    
    def getId(self):
        return self.__id
    def getTitle(self):
        return self.__title
    def getDescription(self):
        return self.__description
    def getDate(self):
        return self.__date
    
    def changeTitle(self, new_title):
        self.__title = new_title
    def changeDescription(self, new_desc):
        self.__description = new_desc
    def changeDate(self, new_date):
        self.__date = new_date
    
    
import abc

class Work(abc.ABC):
    iid: int = 0

    @abc.abstractmethod
    def __init__(self, type, title, author, ISBN):
        Work.iid += 1
        self.__id = Work.iid
        self.__type = type
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
    
    def getTitle(self):
        return self.__title
    def getAuthor(self):
        return self.__author
    def getId(self):
        return self.__id
    def getType(self):
        return self.__type
    
class Book(Work):
    def __init__(self, title, author, ISBN, pages):
        type = "book"
        super().__init__(type, title, author, ISBN)
        self.__pages = pages

    def getTitle(self):
        return self._Work__title
    def getAuthor(self):
        return self._Work__author
    def getId(self):
        return self._Work__id
    def getType(self):
        return self._Work__type

class Ebook(Book):
    def __init__(self, title, author, ISBN, pages, format):
        super().__init__(title, author, ISBN, pages)
        self.__format = format
        self._Work__type = "ebook"

    def getTitle(self):
        return self._Work__title
    def getAuthor(self):
        return self._Work__author
    def getId(self):
        return self._Work__id
    def getType(self):
        return self._Work__type

class Audiobook(Work):
    def __init__(self, title, author, ISBN, minutes):
        type = "audiobook"
        super().__init__(type, title, author, ISBN)
        self.__minutes = minutes

    def getTitle(self):
        return self._Work__title
    def getAuthor(self):
        return self._Work__author
    def getId(self):
        return self._Work__id
    def getType(self):
        return self._Work__type


class Zamowienie():
    id: int = 0

    def __init__(self, bookid, amount):
        Zamowienie.id += 1
        self.__id = Zamowienie.id
        self.__bookid = bookid
        self.__amount = amount
    
    def info(self, oferta):
        for typ in oferta:
            for element in oferta[typ]:
                if element.getId() == self.__bookid:
                    if element.getType() == "book": type = "Książka"
                    elif element.getType() == "ebook": type = "E-book"
                    else: type = "Audiobook"
                    return f"Zamówienie nr {self.__id}:\n{type} o id {element.getId()}\n{element.getTitle()} {element.getAuthor()}\nZamówiona ilość: {self.__amount}"
                    

        

        

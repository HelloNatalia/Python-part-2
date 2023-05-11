class Czytelnik:
    id: int = 0

    def __init__(self,
                 imie: str, nazwisko: str, wiek: int, miasto: str, rok_urodzenia: int):
        Czytelnik.id += 1

        self.__id = Czytelnik.id
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek
        self.__miasto = miasto
        self.__rok_urodzenia = rok_urodzenia

    def pobierz_id(self):
        return self.__id
    def pobierz_imie(self):
        return self.__imie
    def pobierz_nazwisko(self):
        return self.__nazwisko
    def pobierz_wiek(self):
        return self.__wiek
    def pobierz_miasto(self):
        return self.__miasto
    def pobierz_rok_urodzenia(self):
        return self.__rok_urodzenia


class Czytelnik:
    id: int = 0

    def __init__(self,
                 imie: str, nazwisko: str, wiek: int, miasto: str, rok_urodzenia: int):
        Czytelnik.id += 1

        self.id = Czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.miasto = miasto
        self.rok_urodzenia = rok_urodzenia
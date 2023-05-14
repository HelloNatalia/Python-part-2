import Work


# Tworzenie książek
book1 = Work.Book("W pustyni i w puszczy", "Henryk Sienkiewicz", "978-83-240-2959-4", 460)
book2 = Work.Book("Pozwól mi wrócić", "B.A. Paris", "973-83-244-2959-2", 310)
book3 = Work.Book("Na skraju załamania", "B.A. Paris", "938-83-244-2955-4", 290)


ebook1 = Work.Ebook("W pustyni i w puszczy", "Henryk Sienkiewicz", "978-83-240-2959-5", 460, "EPUB")
ebook2 = Work.Ebook("Za zamkniętymi drzwiami", "B.A. Paris", "978-33-540-6959-5", 340, "MOBI")


audiobook1 = Work.Audiobook("W pustyni i w puszczy", "Henryk Sienkiewicz", "978-83-240-2959-4", 600)
audiobook2 = Work.Audiobook("Za zamkniętymi drzwiami", "B.A. Paris", "978-33-540-6959-6", 530)
audiobook3 = Work.Audiobook("Na skraju załamania", "B.A. Paris", "938-83-244-2955-1", 450)
audiobook4 = Work.Audiobook("Pozwól mi wrócić", "B.A. Paris", "973-83-244-2959-7", 600)

oferta = {
    "Książki" : [book1, book2, book3],
    "E-booki" : [ebook1, ebook2],
    "Audiobooki" : [audiobook1, audiobook2, audiobook3, audiobook4]
}

def menu():
    print("\n\n1. Książki w naszej ofercie\n2. Stwórz zamówienie\n3. Zobacz złożone zamówienia\n0. Koniec programu")

zamowienia = []

while True:
    menu()
    op = int(input("\nWybierz operację: "))
    if op == 0:
        break
    elif op == 1:
        for typ in oferta:
            print(f"\n{typ}: ")
            for element in oferta[typ]:
                print(f"Id: {element.getId()} - \"{element.getTitle()}\" {element.getAuthor()}")
    elif op == 2:
        
        id = int(input("Wpisz id książki/ebooka/audiobooka, który chcesz zamówić: "))
        amount = int(input("Wpisz ilość: "))
        order = Work.Zamowienie(id, amount)
        zamowienia.append(order)
    elif op == 3:
        print("\nZamówienia: ")
        for order in zamowienia:
            print(order.info(oferta))

# Wyświetla wszystko w zamóieniach jako audiobook
# złe id - pokazuje ostatnie

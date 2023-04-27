list = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
letter = input("Wpisz literę na jaką mam wypisać słowa z listy: ")
for i in list:
    if i[0:1] == letter:
        print(i, end=" ")
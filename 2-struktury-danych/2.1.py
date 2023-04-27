krotka = (10, -3, 4, 9, 12, -6, 0)
min = krotka[0]
max = krotka[0]

for i in krotka:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Największa liczba w krotce to {max}, a najmniejsza to {min}")
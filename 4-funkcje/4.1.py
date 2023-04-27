def menu():
    print("\n\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie\n0. Koniec programu")

def dodawanie(a, b):
    print(f"\nSuma wynosi: {a+b}")

def odejmowanie(a, b):
    print(f"\nRóżnica wynosi: {a-b}")

def mnozenie(a, b):
    print(f"\nIloczyn wynosi: {a*b}")

def dzielenie(a, b):
    if b != 0:
        print(f"\nDzielenie wynosi: {a/b}")
    else:
        print("\nNie można dzielić przez 0!")


while True:
    menu()
    op = int(input("\nWybierz operację: "))
    if op == 0:
        break
    elif op == 1:
        dodawanie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 2:
        odejmowanie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 3:
        mnozenie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 4:
        dzielenie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    
    



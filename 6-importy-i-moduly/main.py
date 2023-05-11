import calc


while True:
    calc.menu()
    op = int(input("\nWybierz operację: "))
    if op == 0:
        break
    elif op == 1:
        calc.dodawanie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 2:
        calc.odejmowanie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 3:
        calc.mnozenie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    elif op == 4:
        calc.dzielenie(int(input("Liczba a: ")), int(input("Liczba b: ")))
    
    



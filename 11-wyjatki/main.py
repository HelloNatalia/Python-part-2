import calc


while True:
    calc.menu()

    try:
        op = int(input("\nWybierz operację: "))
        if op == 0:
            break
        elif op == 1:
            calc.dodawanie(float(input("Liczba a: ")), float(input("Liczba b: ")))
        elif op == 2:
            calc.odejmowanie(float(input("Liczba a: ")), float(input("Liczba b: ")))
        elif op == 3:
            calc.mnozenie(float(input("Liczba a: ")), float(input("Liczba b: ")))
        elif op == 4:
            calc.dzielenie(float(input("Liczba a: ")), float(input("Liczba b: ")))
        else:
            print("Wybrano nieprawidłową operację, wybierz ponownie.")
    except ValueError:
        print("Wprowadzono błędne dane")
    except Exception as e:
        print("Nieoczekiwany błąd:", str(e))
    
    



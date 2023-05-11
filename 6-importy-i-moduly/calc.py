def menu():
    """Wyświetla menu"""
    print("\n\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie\n0. Koniec programu")

def dodawanie(a: float, b: float) -> None:
    """Wyświetla sumę"""
    print(f"\nSuma wynosi: {a+b}")

def odejmowanie(a: float, b: float) -> None:
    """Wyświetla różnicę"""
    print(f"\nRóżnica wynosi: {a-b}")

def mnozenie(a: float, b: float) -> None:
    """Wyświetla iloczyn"""
    print(f"\nIloczyn wynosi: {a*b}")

def dzielenie(a: float, b: float) -> None:
    """Wyświetla iloraz"""
    if b != 0:
        print(f"\nDzielenie wynosi: {a/b}")
    else:
        print("\nNie można dzielić przez 0!")
import random

print("Gra w zgadnij liczbę!!!\n")

play = True
while play == True:
    amount = 1
    number = random.randint(0, 100)
    user_number = int(input("\nTwoja liczba: "))
    while user_number != number:
        if user_number > number:
            print("Szukana liczba jest mniejsza")
        elif user_number < number:
            print("Szukana liczba jest większa")
        user_number = int(input("Twoja liczba: "))
        amount+=1
    print(f"Gratulacje! Zgadłeś za {amount} razem!")
    if input("Wpisz TAK jeżeli chcesz grać jeszcze raz: ") != "TAK":
        play = False

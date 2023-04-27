word = input("Wpisz słowo a ja sprawdzę czy jest palindromem: ")
word = word.lower()
print(word)
temp = word[::-1]
if temp == word:
    print("Podane słowo jest palindromem :)")
else:
    print("Podane słowo nie jest palindromem :()")
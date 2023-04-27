age = int(input("Ile masz lat?: "))

# if age >= 24:
#     print("Możesz przystąpić do egzaminu.")
# elif(age >= 20 and input("Czy masz kategorię A2? Wpisz \"TAK\" jeżeli masz: ") == "TAK" \
#     and input("Czy masz kategorię A2 conajmniej 2 lata? Wpisz \"TAK\" jeżeli masz:") == "TAK"):
#     print("Możesz przystąpić do egzaminu.")
# else:
#     print("Nie możesz przystąpić do egzaminu.")

# krócej:
if (age >= 24 or age >= 20 and input("Czy masz kategorię A2? Wpisz \"TAK\" jeżeli masz: ") == "TAK" \
    and input("Czy masz kategorię A2 conajmniej 2 lata? Wpisz \"TAK\" jeżeli masz:") == "TAK"):
    print("Możesz przystąpić do egzaminu.")
else:
    print("Nie możesz przystąpić do egzaminu.")
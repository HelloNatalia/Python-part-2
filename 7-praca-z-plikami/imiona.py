from os import path

dir_path = path.dirname(__file__)
filename1 = "imiona.txt"
filename2 = "nazwiska.txt"
new_filename = "result.txt"
data_path1 = path.join(dir_path, filename1)
data_path2 = path.join(dir_path, filename2)
data_path3 = path.join(dir_path, new_filename)

if not path.exists(data_path1) and not path.exists(data_path2):
    exit()

with open(data_path1, "r", encoding="utf-8") as f:
    file_lines_names = f.readlines()
    f.close()

with open(data_path2, "r", encoding="utf-8") as f:
    file_lines_surnames = f.readlines()
    f.close()

# usunięcie "\n" z elementów list
for i in range (len(file_lines_names)):
    file_lines_names[i] = file_lines_names[i].strip()

for i in range (len(file_lines_surnames)):
    file_lines_surnames[i] = file_lines_surnames[i].strip()

max_amount = len(file_lines_names) * len(file_lines_surnames)

# zarządzanie wyjątkiem, gdy użytkownik wpisze co innego niż int
try:
    while True:
        user_amount = int(input("Wpisz ile chcesz wygenerować kombinacji: "))
        if user_amount <= max_amount:
            break
        else:
            print(f"Maksymalnie możesz wpisać {max_amount} kombinacji!")
except:
    print("Wpisanie liczby nie powiodło się")
    exit()

combinations = []

for name in file_lines_names:
        if(len(combinations) == user_amount): break
        for surname in file_lines_surnames:
            combinations.append(name + " " + surname)
            if(len(combinations) == user_amount): break

with open(data_path3, "w", encoding="utf-8") as f:
    for combination in combinations:
        f.write(combination + "\n")
    f.close()

print("Oto twoja lista kombinacji :)")
for i in range (len(combinations)):
    print(f"{i+1}. {combinations[i]}")

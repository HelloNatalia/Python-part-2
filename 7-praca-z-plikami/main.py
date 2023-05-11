from os import path

dir_path = path.dirname(__file__)
filename = "text.txt"
data_path = path.join(dir_path, filename)

if not path.exists(data_path):
    exit()

with open(data_path, "r", encoding="utf-8") as f:
    file_lines = f.readlines()
    f.close()

words = []
for lines in file_lines:
    words += lines.split()

amount = len(words)
print(f"W tekście jest {amount} słów.")

end_letter = []
for word in words:
    letter = word[-1]
    if letter not in end_letter and letter.isalpha():
        end_letter.append(letter)


statistics = {}
for letter in end_letter:
    statistics[letter] = sum(word.endswith((letter)) for word in words)

print(statistics)

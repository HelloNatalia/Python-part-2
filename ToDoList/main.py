from List import List
from datetime import date, timedelta, datetime
import json
import list_operations

def menu():
    print("\n\n1. Dodaj nowe zadanie\n2. Wyświetl całą listę zadań\n3. Wyświetl konkretne zadanie\n4. Wyświetl zadania przypisane do konkretnego dnia tygodnia\n5. Wyświetl zadania przypisane do konkretnej daty\n6. Wyświetl zadania przypisane do konkretnego tygodnia\n7. Usuń zadanie\n8. Aktualizuj zadanie\n9. Przypisz zadanie do konkretnego dnia\n10. Zapisz do pliku\n0. Koniec programu")

list = list_operations.loadListFromJsonFile('lista.json')

print("Twoja lista do zrobienia: ")
if len(list) != 0:
    for task in list:
        print(task.showTask())
else:
    print("Nie ma żadnych zadań na liście.")


while True:
    try:
        menu()
        op = int(input("\nWybierz operację: "))
        if op == 0:
            with open("lista.json", "w") as file:
                json.dump(list, file, cls=list_operations.ListEncoder)
            break
        elif op == 1:
            task = List.createTask()
            list.append(task)
        elif op == 2:
            list_operations.showList(list)
        elif op == 3:
            try:
                task_id = int(input("Które zadanie chcesz wyświetlić? podaj jego id: "))
                list_operations.showSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 4:
                list_operations.showTasksFromSpecificDay(list)
        elif op == 5:
                list_operations.showTasksFromSpecificDate(list)
        elif op == 6:
                list_operations.showTasksFromSpecificWeek(list)
        elif op == 7:
            try:
                task_id = int(input("Które zadanie chcesz usunąć? podaj jego id: "))
                list_operations.deleteSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 8:
            try:
                task_id = int(input("Które zadanie chcesz zaktualizować? podaj jego id: "))
                list_operations.updateSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 9:
            try:
                task_id = int(input("Które zadanie chcesz przypisać do konkretnego dnia tygodnia? podaj jego id: "))
                list_operations.addDayToDo(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 10:
            with open("lista.json", "w") as file:
                json.dump(list, file, cls=list_operations.ListEncoder)
        else:
            print("Wprowadzono niepoprawny numer operacji")
    except ValueError:
        print("Wprowadzono niepoprawny numer operacji")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        
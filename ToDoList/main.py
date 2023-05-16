from List import List
import json

# Do zapisywania i odczytywania jsona #
class ListEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, List):
            return obj.__dict__
        return super().default(obj)
    
class ListDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if '_List__id' in dct and '_List__title' in dct and '_List__description' in dct and '_List__date' in dct:
            return List(dct['_List__title'], dct['_List__description'], dct['_List__date'])
        return dct

def loadListFromJsonFile(filename):
    with open(filename, 'r') as file:
        data = json.load(file, cls=ListDecoder)
        return data
# # # # # # # # # # # # # # # # # # #

def menu():
    print("\n\n1. Dodaj nowe zadanie\n2. Wyświetl listę zadań\n3. Wyświetl zadanie\n4. Usuń zadanie\n5. Aktualizuj zadanie\n6. Zapisz do pliku\n0. Koniec programu")

list = loadListFromJsonFile('lista.json')

def showList(list) -> None:
    """Wyświetla listę todo"""
    show_desc = ""
    if len(list) != 0:
        while show_desc != "t" and show_desc != "n":
            show_desc = input("Czy pokazać opisy zadań? (t/n):")
        for task in list:
            print(task.showTask())
            if show_desc == "t":
                print(f"\t{task.getDescription()}")
    else:
        print("Nie ma żadnych zadań na liście.")

def deleteSpecificTask(list, task_id) -> None:
    """Usuwa zadanie"""
    i = 0
    found = False
    for task in list:
        if task.getId() == task_id:
            del list[i]
            found = True
            break
        else: found = False
        i += 1
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")

def showSpecificTask(list, task_id) -> None:
    """Pokazuje konkretne zadanie"""
    found = False
    for task in list:
        if task.getId() == task_id:
            print(task.showTask())
            print(f"\t{task.getDescription()}")
            found = True
            break
        else: found = False
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")

def updateSpecificTask(list, task_id) -> None:
    """Aktualizuje konkretne zadanie"""
    i = 0
    found = False
    for task in list:
        if task.getId() == task_id:

            while True:
                change_title = input("Czy chcesz zmienić tytuł zadania? (t/n): ")
                if change_title == "t": new_title = input("Wpisz nowy tytuł: ")
                elif change_title == "n": new_title = task.getTitle()
                change_desc = input("Czy chcesz zmienić opis zadania? (t/n): ")
                if change_desc == "t": new_desc = input("Wpisz nowy tytuł: ")
                elif change_desc == "n": new_desc = task.getDescription()
                change_date = input("Czy chcesz zmienić date zadania? (t/n): ")
                if change_date == "t": new_date = List.date()
                elif change_date == "n": new_date = task.getDate()
                if new_title and new_desc and new_date: break
            # list[i] = List(new_title, new_desc, new_date)
            task.changeTitle(new_title)
            task.changeDescription(new_desc)
            task.changeDate(new_date)
            found = True
            break
        else: found = False
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")

print("Twoja lista do zrobienia:")
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
                json.dump(list, file, cls=ListEncoder)
            break
        elif op == 1:
            task = List.createTask()
            list.append(task)
        elif op == 2:
            showList(list)
        elif op == 3:
            try:
                task_id = int(input("Które zadanie chcesz wyświetlić? podaj jego id: "))
                showSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 4:
            try:
                task_id = int(input("Które zadanie chcesz usunąć? podaj jego id: "))
                deleteSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 5:
            try:
                task_id = int(input("Które zadanie chcesz zaktualizować? podaj jego id: "))
                updateSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 6:
            with open("lista.json", "w") as file:
                json.dump(list, file, cls=ListEncoder)
        else:
            print("Wprowadzono niepoprawny numer operacji")
    except ValueError:
        print("Wprowadzono niepoprawny numer operacji")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        
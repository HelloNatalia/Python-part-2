from List import List
from datetime import date, timedelta, datetime
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
        if '_List__id' in dct and '_List__title' in dct and '_List__description' in dct and '_List__date' in dct and '_List__daytodo' in dct and '_List__day_of_week' in dct:
            return List(dct['_List__title'], dct['_List__description'], dct['_List__date'], dct['_List__daytodo'], dct['_List__day_of_week'])
        return dct

def loadListFromJsonFile(filename):
    with open(filename, 'r') as file:
        data = json.load(file, cls=ListDecoder)
        return data
# # # # # # # # # # # # # # # # # # #

def menu():
    print("\n\n1. Dodaj nowe zadanie\n2. Wyświetl całą listę zadań\n3. Wyświetl konkretne zadanie\n4. Wyświetl zadania przypisane do konkretnego dnia tygodnia\n5. Wyświetl zadania przypisane do konkretnej daty\n6. Wyświetl zadania przypisane do konkretnego tygodnia\n7. Usuń zadanie\n8. Aktualizuj zadanie\n9. Przypisz zadanie do konkretnego dnia\n10. Zapisz do pliku\n0. Koniec programu")

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
                if change_desc == "t": new_desc = input("Wpisz nowy opis: ")
                elif change_desc == "n": new_desc = task.getDescription()
                change_date = input("Czy chcesz zmienić date zadania? (t/n): ")
                if change_date == "t": new_date = List.date()
                elif change_date == "n": new_date = task.getDate()
                change_daytodo = input("Czy chcesz zmienić przypisanie zadania do dnia? (t/n): ")
                if change_daytodo == 't': 
                    new_daytodo_info = task.dayToDo(new_date)
                    new_daytodo = new_daytodo_info[1]
                    new_day_of_week = new_daytodo_info[0]
                elif change_daytodo == 'n':
                    new_daytodo = task.getDaytodo()
                    new_day_of_week = task.getDay_of_week()
                if new_title and new_desc and new_date and new_daytodo != None and new_day_of_week != None: break
            # list[i] = List(new_title, new_desc, new_date)
            task.changeTitle(new_title)
            task.changeDescription(new_desc)
            task.changeDate(new_date)
            task.changeDaytodo(new_daytodo, new_day_of_week)
            found = True
            break
        else: found = False
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")

def addDayToDo(list, task_id) -> None:
    """Przypisuje lub zmienia datę, do której przypisane jest zadanie"""
    found = False
    for task in list:
        if task.getId() == task_id:
            found = True
            if task.getDaytodo() and task.getDay_of_week():
                change = input("To zadanie ma już przypisaną datę, czy chcesz ją zmienić? (t/n)")
                while True:
                    if change == 't':
                        new_daytodo_info = task.dayToDo(task.getDate())
                        new_daytodo = new_daytodo_info[1]
                        new_day_of_week = new_daytodo_info[0]
                        task.changeDaytodo(new_daytodo, new_day_of_week)
                        break
                    if change == 'n':
                        break
            else:
                new_daytodo_info = task.dayToDo(task.getDate())
                new_daytodo = new_daytodo_info[1]
                new_day_of_week = new_daytodo_info[0]
                task.changeDaytodo(new_daytodo, new_day_of_week)
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")
    
def showTasksFromSpecificDay(list):
    daytodo_list = []
    today = date.today()
    future_date = today + timedelta(days=6)
    while True:
        day = input("Wpisz z jakiego dnia tygodnia chcesz wyświetlić zadania (obowiązują dni od dzisiaj do 6 w przód): ")
        day = day.capitalize()
        if day in List.week:
            for task in list:
                if task.getDaytodo() != None and task.getDay_of_week() != None:
                    date_format = "%d-%m-%Y"
                    daytodo = datetime.strptime(task.getDaytodo(), date_format).date()
                    if List.week[task.getDay_of_week()] == day and today <= daytodo <= future_date:
                        daytodo_list.append(task)
            break
    if len(daytodo_list) != 0:
        for task in daytodo_list:
            print(task.showTask())
    else:
        print("Nie ma żadnych zadań na liście w tym dniu.")

def showTasksFromSpecificDate(list):
    daytodo_list = []
    date = List.date()
    for task in list:
        if task.getDaytodo() == date:
            daytodo_list.append(task)
    if len(daytodo_list) != 0:
        for task in daytodo_list:
            print(task.showTask())
    else:
        print("Nie ma żadnych zadań na liście w tym dniu.")
        
def showTasksFromSpecificWeek(list):
    week_list = [[],[],[],[],[],[],[]]
    print("Podaj datę rozpoczęcia tygodnia, od tej daty pokażą się przypisane zadania do wykonania na 7 dni w przód.")
    date = List.date()
    date_format = "%d-%m-%Y"
    date_start = datetime.strptime(date, date_format).date()
    # date_end = date_start + timedelta(days=6)
    for i in range(7):
        for task in list:
            if task.getDaytodo() and task.getDay_of_week:
                daytodo = datetime.strptime(task.getDaytodo(), date_format).date()
                if daytodo == date_start:
                    week_list[i].append(task)
        date_start = date_start + timedelta(days=1)
    
    # for day in week_list:
    #     for task in week_list[day]:
    #         print(task.showTask())
    
    for day in week_list:
        for i in range(len(day)):
            print(day[i].showTask())





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
                showTasksFromSpecificDay(list)
        elif op == 5:
                showTasksFromSpecificDate(list)
        elif op == 6:
                showTasksFromSpecificWeek(list)
        elif op == 7:
            try:
                task_id = int(input("Które zadanie chcesz usunąć? podaj jego id: "))
                deleteSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 8:
            try:
                task_id = int(input("Które zadanie chcesz zaktualizować? podaj jego id: "))
                updateSpecificTask(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 9:
            try:
                task_id = int(input("Które zadanie chcesz przypisać do konkretnego dnia tygodnia? podaj jego id: "))
                addDayToDo(list, task_id)
            except ValueError:
                print("Wprowadzono błędne id")
        elif op == 10:
            with open("lista.json", "w") as file:
                json.dump(list, file, cls=ListEncoder)
        else:
            print("Wprowadzono niepoprawny numer operacji")
    except ValueError:
        print("Wprowadzono niepoprawny numer operacji")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        
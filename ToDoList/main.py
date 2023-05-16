from List import List

def menu():
    print("\n\n1. Dodaj nowe zadanie\n2. Wyświetl listę zadań\n3. Wyświetl zadanie\n4. Usuń zadanie\n5. Aktualizuj zadanie\n6. Zapisz do pliku\n0. Koniec programu")

def showList(list):
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

def deleteSpecificTask(list, task_id):
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

def showSpecificTask(list, task_id):
    found = False
    for task in list:
        if task.getId() == task_id:
            print(task.showTask())
            print(f"\t{task.getDescription()}")
            found = True
            break
        else: found = False
    if found == False: print("Nie znaleziono zadania o wprowadzonym id.")

def updateSpecificTask(list, task_id):
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
        

list = []

while True:
    try:
        menu()
        op = int(input("\nWybierz operację: "))
        if op == 0:
            # Zapisanie listy do pliku
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
            pass
        else:
            print("Wprowadzono niepoprawny numer operacji")
    except ValueError:
        print("Wprowadzono niepoprawny numer operacji")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        
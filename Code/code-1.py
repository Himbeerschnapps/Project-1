def todo_list():
    tasks = []

    while True:
        print("1. Добавить дело")
        print("2. Посмотреть список дел")
        print("3. Убрать дело")
        print("4. Завершить работу")

        choice = input("Что бы Вы хотели сделать? (Выберите номер задачи) ")

        if choice == '1':
            task = input("Что Вам нужно сделать? ")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                print("Ваши дела: ")
                for task in tasks:
                    print(task)
            else:
                print("Дел нет! Отдыхайте!")
        elif choice == '3':
            if tasks:
                task = input("Что Вы уже сделали? ")
                if task in tasks:
                    tasks.remove(task)
                    print("Отличная работа!")
                else:
                    print("Таких дел не было.")
            else:
                print("Дел нет! Отдыхайте!")
        elif choice == '4':
            break
        else:
            print("Попробуйте ещё раз!")

todo_list()

n = input()
if n == "фильм" or n == "лучший фильм":
    v = input("Выбирите жанр: \n"
              "комедия\n"
              "боевик\n"
              "ужастик\n"
              ":")
    if v == "комедия":
        b = input("Введите год: ")
        if b == "2018":
            print("Душа Компании")
        elif b == "2019":
            print("Отпетые мошенницы")
        elif b == "2020":
            print("Гламурные боссы")
        elif b == "2021" or b == "2017":
            c = input("Введите год еще раз: ")
            if c == "2018":
                print("Душа Компании")
            elif c == "2019":
                print("Отпетые мошенницы")
            elif c == "2020":
                print("Гламурные боссы")

    if v == "боевик":
        b = input("Введите год: ")
        if b == "2018":
            print("Мег:Монстр")
        elif b == "2019":
            print("Гемини")
        elif b == "2020":
            print("Скайлайн 3")
        elif b == "2021" or b == "2017":
            c = input("Введите год еще раз: ")
            if c == "2018":
                print("Мег:Монстр")
            elif c == "2019":
                print("Гемини")
            elif c == "2020":
                print("Скайлайн 3")
    if v == "ужастик":
        b = input("Введите год: ")
        if b == "2018":
            print("Правда или действие")
        elif b == "2019":
            print("Эбигейл")
        elif b == "2020":
            print("Эмма")
        elif b == "2021" or b == "2017":
            c = input("Введите год еще раз: ")
            if c == "2018":
                print("Правда или действие")
            elif c == "2019":
                print("Эбигейл")
            elif c == "2020":
                print("Эмма")

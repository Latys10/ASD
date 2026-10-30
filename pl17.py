# ============================================================
# Лабораторная №17. ЦИКЛИЧЕСКИЙ (КОЛЬЦЕВОЙ) СПИСОК (без функций def)
# Условие сортировки: УБЫВАНИЕ суммы цифр дробной части числа.
# Односвязный кольцевой список: последний узел указывает на первый.
# Храним только tail; голова = tail["next"]. Признака None-конца нет,
# поэтому обход ведём по счётчику size.
# ============================================================

tail = None                      # последний узел кольца (None = кольцо пустое)
size = 0                         # количество элементов
to_add = []                      # очередь добавления: (число, позиция); 0=начало, -1=конец, k=индекс

print("Вводите числа по одному (пустая строка - конец ввода):")  # N заранее неизвестно
while True:
    s = input("> ").strip().replace(",", ".")
    if s == "":
        break
    try:
        to_add.append((float(s), -1))
    except ValueError:
        print("Это не число, повторите")

while True:                      # главный цикл (меню)

    # ---------- ДОБАВЛЕНИЕ ----------
    for value, pos in to_add:
        s = str(abs(value))
        key = 0                  # сумма цифр дробной части
        if "." in s:
            for ch in s.split(".")[1]:
                if ch.isdigit():
                    key += int(ch)
        node = {"data": value, "key": key, "next": None}   # новый узел

        if tail is None:                 # кольцо пустое
            node["next"] = node          # единственный узел указывает сам на себя
            tail = node                  # он же и хвост
        elif pos == 0:                   # вставка в начало (перед головой)
            node["next"] = tail["next"]  # новый указывает на старую голову
            tail["next"] = node          # хвост теперь указывает на новую голову; tail не меняется
        elif pos == -1 or pos == size:   # вставка в конец
            node["next"] = tail["next"]  # новый замыкает кольцо на голову
            tail["next"] = node          # старый хвост указывает на новый
            tail = node                  # новый узел - хвост
        else:                            # вставка в середину
            prev = tail["next"]          # начинаем с головы
            for _ in range(pos - 1):     # pos-1 шагов
                prev = prev["next"]
            node["next"] = prev["next"]  # новый указывает на следующий за prev
            prev["next"] = node          # prev указывает на новый
        size += 1
    to_add = []

    # ---------- ВЫВОД (ровно size шагов, иначе зациклимся) ----------
    items = []
    if tail is not None:
        cur = tail["next"]               # начинаем с головы
        for _ in range(size):            # обходим size узлов
            items.append(str(cur["data"]))
            cur = cur["next"]
    print("\nКольцо:", " -> ".join(items) + " -> (снова к первому)" if items else "пусто")
    print("Размер:", size)

    # ---------- МЕНЮ ----------
    print("1-в начало  2-в конец  3-по индексу  4-удалить по значению  5-удалить по индексу  6-сортировать  0-выход")
    choice = input("Выбор: ").strip()

    target = None                # удаляемый узел
    before = None                # узел перед удаляемым

    if choice == "0":
        break

    elif choice in ("1", "2", "3"):
        try:
            v = float(input("Число: ").replace(",", "."))
            if choice == "1":
                to_add.append((v, 0))
            elif choice == "2":
                to_add.append((v, -1))
            else:
                i = int(input("Индекс (0.." + str(size) + "): "))
                if 0 <= i <= size:
                    to_add.append((v, i))
                else:
                    print("Неверный индекс")
        except ValueError:
            print("Ошибка ввода")

    elif choice == "4":          # поиск по значению
        try:
            v = float(input("Какое число удалить: ").replace(",", "."))
            if tail is not None:
                before = tail                # узел перед головой - хвост
                cur = tail["next"]           # текущий = голова
                for _ in range(size):        # максимум size проверок
                    if cur["data"] == v:
                        target = cur         # нашли
                        break
                    before = cur             # сдвигаем «предыдущий»
                    cur = cur["next"]
            if target is None:
                print("Не найдено")
        except ValueError:
            print("Ошибка ввода")

    elif choice == "5":          # поиск по индексу
        try:
            i = int(input("Индекс (0.." + str(size - 1) + "): "))
            if 0 <= i < size:
                before = tail                # перед головой стоит хвост
                target = tail["next"]        # голова
                for _ in range(i):           # идём i шагов
                    before = target
                    target = target["next"]
            else:
                print("Неверный индекс")
        except ValueError:
            print("Ошибка ввода")

    elif choice == "6":          # сортировка по убыванию суммы цифр дробной части
        if size >= 2:
            swapped = True
            while swapped:
                swapped = False
                cur = tail["next"]           # начинаем с головы
                for _ in range(size - 1):    # size-1 сравнений соседних пар
                    nxt = cur["next"]
                    if cur["key"] < nxt["key"]:      # нужен обмен для убывания
                        cur["data"], nxt["data"] = nxt["data"], cur["data"]
                        cur["key"], nxt["key"] = nxt["key"], cur["key"]
                        swapped = True
                    cur = nxt
        print("Отсортировано")

    else:
        print("Неизвестная команда")

    # ---------- УДАЛЕНИЕ узла target (общий блок для команд 4 и 5) ----------
    if target is not None:
        if size == 1:                        # удаляем единственный узел
            tail = None                      # кольцо становится пустым
        else:
            before["next"] = target["next"]  # предыдущий перескакивает через target
            if target is tail:               # удалили хвост
                tail = before                # новым хвостом станет предыдущий
        size -= 1
        print("Удалено")
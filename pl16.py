# ============================================================
# Лабораторная №16. ДВУСВЯЗНЫЙ СПИСОК (без функций def)
# Условие сортировки: УБЫВАНИЕ суммы цифр дробной части числа.
# Узел = словарь {"data", "key", "prev", "next"}; храним head и tail.
# ============================================================

head = None                      # первый узел списка
tail = None                      # последний узел списка (позволяет быстро добавлять в конец)
size = 0                         # количество элементов
to_add = []                      # очередь добавления: пары (число, позиция); 0=начало, -1=конец, k=индекс

print("Вводите числа по одному (пустая строка - конец ввода):")  # N заранее неизвестно
while True:                      # ввод начальной последовательности
    s = input("> ").strip().replace(",", ".")   # читаем строку
    if s == "":                  # пустая строка = конец
        break
    try:
        to_add.append((float(s), -1))   # число в очередь, добавим в конец
    except ValueError:
        print("Это не число, повторите")

while True:                      # главный цикл (меню)

    # ---------- ДОБАВЛЕНИЕ ----------
    for value, pos in to_add:    # обрабатываем очередь
        s = str(abs(value))      # число без знака как строка
        key = 0                  # сумма цифр дробной части
        if "." in s:             # есть ли дробная часть
            for ch in s.split(".")[1]:   # цифры после точки
                if ch.isdigit():
                    key += int(ch)       # суммируем
        node = {"data": value, "key": key, "prev": None, "next": None}   # новый узел

        if head is None:                 # список пуст
            head = node                  # узел и первый, и последний
            tail = node
        elif pos == 0:                   # вставка в начало
            node["next"] = head          # новый узел смотрит вперёд на старую голову
            head["prev"] = node          # старая голова смотрит назад на новый узел
            head = node                  # новая голова
        elif pos == -1 or pos == size:   # вставка в конец
            node["prev"] = tail          # новый узел смотрит назад на старый хвост
            tail["next"] = node          # старый хвост смотрит вперёд на новый узел
            tail = node                  # новый хвост
        else:                            # вставка в середину по индексу
            before = head                # узел, после которого вставляем
            for _ in range(pos - 1):     # pos-1 шагов вперёд
                before = before["next"]
            after = before["next"]       # узел, перед которым вставляем
            node["prev"] = before        # 4 связи: новый <- before
            node["next"] = after         # новый -> after
            before["next"] = node        # before -> новый
            after["prev"] = node         # after <- новый
        size += 1                        # размер вырос
    to_add = []                  # очередь пуста

    # ---------- ВЫВОД (вперёд и назад) ----------
    items = []                   # значения от головы к хвосту
    cur = head
    while cur is not None:       # обход вперёд по next
        items.append(str(cur["data"]))
        cur = cur["next"]
    back = []                    # значения от хвоста к голове
    cur = tail
    while cur is not None:       # обход назад по prev (возможен только в двусвязном списке)
        back.append(str(cur["data"]))
        cur = cur["prev"]
    print("\nВперёд:", " <-> ".join(items) if items else "пуст")
    print("Назад: ", " <-> ".join(back) if back else "пуст")
    print("Размер:", size)

    # ---------- МЕНЮ ----------
    print("1-в начало  2-в конец  3-по индексу  4-удалить по значению  5-удалить по индексу  6-сортировать  0-выход")
    choice = input("Выбор: ").strip()

    target = None                # узел, который нужно удалить (если будет выбран)

    if choice == "0":            # выход
        break

    elif choice in ("1", "2", "3"):      # добавление
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

    elif choice == "4":          # поиск узла для удаления по значению
        try:
            v = float(input("Какое число удалить: ").replace(",", "."))
            cur = head
            while cur is not None:           # ищем первое совпадение
                if cur["data"] == v:
                    target = cur             # запоминаем найденный узел
                    break
                cur = cur["next"]
            if target is None:
                print("Не найдено")
        except ValueError:
            print("Ошибка ввода")

    elif choice == "5":          # поиск узла для удаления по индексу
        try:
            i = int(input("Индекс (0.." + str(size - 1) + "): "))
            if 0 <= i < size:
                target = head
                for _ in range(i):           # идём i шагов от головы
                    target = target["next"]
            else:
                print("Неверный индекс")
        except ValueError:
            print("Ошибка ввода")

    elif choice == "6":          # сортировка (пузырёк по убыванию суммы цифр дробной части)
        if size >= 2:
            swapped = True
            while swapped:
                swapped = False
                cur = head
                while cur["next"] is not None:
                    nxt = cur["next"]
                    if cur["key"] < nxt["key"]:      # нужен обмен для убывания
                        cur["data"], nxt["data"] = nxt["data"], cur["data"]
                        cur["key"], nxt["key"] = nxt["key"], cur["key"]
                        swapped = True
                    cur = nxt
        print("Отсортировано")

    else:
        print("Неизвестная команда")

    # ---------- УДАЛЕНИЕ найденного узла target (общий блок для команд 4 и 5) ----------
    if target is not None:                   # если узел для удаления выбран
        if target["prev"] is not None:       # есть предыдущий узел
            target["prev"]["next"] = target["next"]   # предыдущий перескакивает через target
        else:                                # target - голова
            head = target["next"]            # голова сдвигается вперёд
        if target["next"] is not None:       # есть следующий узел
            target["next"]["prev"] = target["prev"]   # следующий ссылается назад мимо target
        else:                                # target - хвост
            tail = target["prev"]            # хвост сдвигается назад
        size -= 1                            # размер уменьшился
        print("Удалено")
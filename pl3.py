text = input("ввод")
error = False

if len(text) == 0:
    error = True
    print("пустой ввод")
else:
    for char in text:
        if char not in "0123456789":
            error = True
            break

    if error == True:
        print("это не число")
    else:
        x = int(text)
        if x < 1:
            print("число должно быть >= 1")
        else:
            results = []
            K = 0
            while 3 ** K <= x:
                L = 0
                while 3 ** K * 5 ** L <= x:
                    M = 0
                    while 3 ** K * 5 ** L * 7 ** M <= x:
                        xi = 3 ** K * 5 ** L * 7 ** M
                        results.append(xi)
                        M = M + 1
                    L = L + 1
                K = K + 1

            print(sorted(results))
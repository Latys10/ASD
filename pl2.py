text = input("ввод ")

if len(text) == 0:
    print("пустой ввод")
else:
    if text[-1] != '=':
        print("нет знака =")
    else:
        expression = text[:-1]
        allowed = "0123456789.+-*/()[]{} "
        error = False 

        for char in expression:
            if char not in allowed:
                error = True
                break

        if error == True:
            print("недопустимый символ")
        else:
            stack = []
            bracket_error = False  

            for char in expression:
                if char in '([{':
                    stack.append(char)
                elif char in ')]}':
                    if len(stack) == 0:
                        bracket_error = True
                        break
                    last_open = stack.pop()
                    if char == ')' and last_open != '(':
                        bracket_error = True
                        break
                    if char == ']' and last_open != '[':
                        bracket_error = True
                        break
                    if char == '}' and last_open != '{':
                        bracket_error = True
                        break

            if bracket_error == True or len(stack) != 0:
                print("неправильные скобки")
            else:
                check_div = expression.replace(" ", "")

                if "/0" in check_div:
                    print("деление на ноль")
                else:
                    expr_ready = ""

                    for char in expression:
                        if char == '[' or char == '{':
                            expr_ready = expr_ready + '('
                        elif char == ']' or char == '}':
                            expr_ready = expr_ready + ')'
                        else:
                            expr_ready = expr_ready + char

                    try:
                        result = eval(expr_ready)
                        print("Результат: ", result)
                    except ZeroDivisionError:
                        print("деление на ноль")
                    except:
                        print("ошибка в выражении")
                        #2+7*(3/9)-5=
                        #4+4/(2-2)=

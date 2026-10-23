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

        if error:
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

            if bracket_error or len(stack) != 0:
                print("неправильные скобки")
            else:
                expr_ready = ""
                for char in expression:
                    if char == '[' or char == '{':
                        expr_ready = expr_ready + '('
                    elif char == ']' or char == '}':
                        expr_ready = expr_ready + ')'
                    else:
                        expr_ready = expr_ready + char

                s = "(" + expr_ready + ")"

                values = []             # стек чисел
                ops = []                # стек операций и скобок
                expect_operand = True   # число ( или унарный минус
                error_msg = ""
                i = 0

                while i < len(s) and error_msg == "":
                    ch = s[i]

                    if ch == ' ':
                        i += 1

                    elif ch.isdigit() or ch == '.':
                        if not expect_operand:
                            error_msg = "ошибка в выражении"   # 2 3
                        else:
                            j = i
                            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                                j += 1
                            number = s[i:j]
                            if number.count('.') > 1 or number == '.':
                                error_msg = "ошибка в выражении"   # 1.2.3
                            else:
                                values.append(float(number))
                                expect_operand = False
                            i = j

                    elif ch == '(':
                        if not expect_operand:
                            error_msg = "ошибка в выражении"   # 2(3)
                        else:
                            ops.append('(')
                            i += 1

                    elif expect_operand:
                        if ch == '-':
                            values.append(0.0)
                            ops.append('-')
                            i += 1
                        elif ch == '+':
                            i += 1
                        else:
                            error_msg = "ошибка в выражении"   #  (), 2+)

                    else:
                        # пришла операция + - * / или закрывающая скобка
                        if ch == '*' or ch == '/':
                            need = 2
                        else:
                            need = 1    # для + - 

                        # считаем операции из стека, пока их приоритет >= need
                        while error_msg == "" and ops[-1] != '(':
                            if ops[-1] == '*' or ops[-1] == '/':
                                top_priority = 2
                            else:
                                top_priority = 1
                            if top_priority < need:
                                break

                            op = ops.pop()
                            b = values.pop()
                            a = values.pop()
                            if op == '+':
                                values.append(a + b)
                            elif op == '-':
                                values.append(a - b)
                            elif op == '*':
                                values.append(a * b)
                            else:
                                if b == 0:
                                    error_msg = "деление на ноль"
                                else:
                                    values.append(a / b)

                        if error_msg == "":
                            if ch == ')':
                                ops.pop()
                            else:
                                ops.append(ch)
                                expect_operand = True
                            i += 1

                if error_msg != "":
                    print(error_msg)
                else:
                    result = values[0]
                    if result == int(result):
                        result = int(result)
                    print("результат:", result)
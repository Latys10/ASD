text = input("ввод")
stack = []
error = False

for char in text:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if len(stack) == 0:
            error = True
            break
        last_open = stack.pop()
        if char == ')' and last_open != '(':
            error = True
            break
        if char == ']' and last_open != '[':
            error = True
            break
        if char == '}' and last_open != '{':
            error = True
            break

if error == False and len(stack) == 0:
    print("строка существует")
else:
    print("строки нету")
    #()[({}())]
    #(]{})
    #([)])
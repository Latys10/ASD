numbers = list(map(float, input("Ввод ").split()))
n = len(numbers)

for i in range(n):
    min = i
    
    for j in range(i + 1, n):
        if numbers[j] < numbers[min]:
            min = j
    numbers[i], numbers[min] = numbers[min], numbers[i]

print("вывод", *numbers)
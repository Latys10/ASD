numbers = list(map(float, input("Ввод ").split()))
n = len(numbers)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        key = numbers[i]
        j = i

        while j >= gap and numbers[j - gap] > key:
            numbers[j] = numbers[j - gap]
            j -= gap
        numbers[j] = key
    gap //= 2

print(*numbers)
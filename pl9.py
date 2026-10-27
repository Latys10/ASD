numbers = list(map(float, input("Ввод ").split()))
n = len(numbers)

for i in range(n // 2 - 1, -1, -1):
    root = i
    
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        
        if left < n and numbers[left] > numbers[largest]:
            largest = left
        if right < n and numbers[right] > numbers[largest]:
            largest = right
        if largest == root:
            break
        numbers[root], numbers[largest] = numbers[largest], numbers[root]
        root = largest
        
for end in range(n - 1, 0, -1):
    numbers[0], numbers[end] = numbers[end], numbers[0]
    root = 0
    
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < end and numbers[left] > numbers[largest]:
            largest = left
        if right < end and numbers[right] > numbers[largest]:
            largest = right
        if largest == root:
            break
        numbers[root], numbers[largest] = numbers[largest], numbers[root]
        root = largest

print(*numbers)
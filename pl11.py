numbers = list(map(float, input("Ввод ").split()))
stack = [(0, len(numbers) - 1)]

while len(stack) > 0:
    low, high = stack.pop()
    
    if low < high:
        mid = (low + high) // 2
        numbers[mid], numbers[high] = numbers[high], numbers[mid]
        pivot = numbers[high]
        i = low - 1
        
        for j in range(low, high):
            
            if numbers[j] <= pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
        p = i + 1
        stack.append((low, p - 1))
        stack.append((p + 1, high))
        
print(*numbers)
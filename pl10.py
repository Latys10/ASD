numbers = list(map(float, input("Ввод ").split()))
n = len(numbers)
width = 1

while width < n:
    result = []
    
    for start in range(0, n, 2 * width):
        left = numbers[start:start + width]
        right = numbers[start + width:start + 2 * width]
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
    numbers = result
    width *= 2

print(*numbers)
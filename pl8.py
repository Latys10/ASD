numbers = list(map(int, input("Ввод ").split()))
min_value = numbers[0]
max_value = numbers[0]

for x in numbers:
    if x < min_value:
        min_value = x
    if x > max_value:
        max_value = x

for i in range(len(numbers)):
    numbers[i] = numbers[i] - min_value

max_value = max_value - min_value
exp = 1
while max_value // exp > 0:
    buckets = [[] for _ in range(10)]
    
    for x in numbers:
        digit = (x // exp) % 10
        buckets[digit].append(x)
    numbers = []

    for bucket in buckets:
        for x in bucket:
            numbers.append(x)
    exp *= 10

for i in range(len(numbers)):
    numbers[i] = numbers[i] + min_value

print(*numbers)
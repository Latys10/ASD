numbers = list(map(float, input("Ввод ").split()))
run_size = 2
runs = []

for start in range(0, len(numbers), run_size):
    chunk = numbers[start:start + run_size]

    for i in range(1, len(chunk)):
        key = chunk[i]
        j = i - 1
        while j >= 0 and chunk[j] > key:
            chunk[j + 1] = chunk[j]
            j -= 1
        chunk[j + 1] = key
    runs.append(chunk)
big = 1
small = 1

while big + small < len(runs):
    big, small = big + small, big
    
while len(runs) < big + small:
    runs.append([])
    
tapes = [runs[:big], runs[big:], []]
phase = 0
print("Начало:", tapes)

while len(tapes[0]) + len(tapes[1]) + len(tapes[2]) > 1:
    out = 0
    for k in range(3):
        if len(tapes[k]) == 0:
            out = k
    ins = [k for k in range(3) if k != out]
    count = min(len(tapes[ins[0]]), len(tapes[ins[1]]))

    for _ in range(count):
        left = tapes[ins[0]].pop(0)
        right = tapes[ins[1]].pop(0)
        result = []
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
        tapes[out].append(result)
    phase += 1
    print("Фаза", phase, ":", tapes)
    
for tape in tapes:
    if len(tape) == 1:
        numbers = tape[0]

print(*numbers)
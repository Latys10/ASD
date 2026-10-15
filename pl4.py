inp = input("Ввод ")
arr = list(map(float, inp.split()))
n = len(arr)
gap = n                
shrink = 1.3         
swapped = True

while gap > 1 or swapped:
    gap = int(gap / shrink)
    if gap < 1:
        gap = 1
    
    swapped = False
    for i in range(n - gap):
        if arr[i] > arr[i + gap]:
            arr[i], arr[i + gap] = arr[i + gap], arr[i]
            swapped = True
            
print("Отсортированная последовательность:", arr)
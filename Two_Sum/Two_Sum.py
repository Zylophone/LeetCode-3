arr = [3,2,4]
target = 6
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if target == arr[i] + arr[j]:
            print(i,j)

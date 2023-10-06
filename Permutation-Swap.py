import math
tc = int(input())

for _ in range(tc):
    size = int(input())
    arr = list(map(int, input().split()))   
    lowest = []
    for i in range(len(arr)):
        if abs(arr[i]-(i+1)) > 0:
            lowest.append(abs(arr[i]-(i+1)))

    print(math.gcd(*lowest))
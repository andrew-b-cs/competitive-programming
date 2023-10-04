tc = int(input())



for _ in range(tc):
    days, diff = map(int, input().split())
    
    daysArr = [int(number) for number in input().split()]
    tempArr = [int(number) for number in input().split()]
    correctedTemps = [None] * days
    
    oldOrder = list(range(days))
    
    oldOrder.sort(key=(lambda x: daysArr[x]))
    tempArr.sort()
    
    for i in range(days):
        correctedTemps[oldOrder[i]] = tempArr[i] # type: ignore
    print(*correctedTemps)
    

     
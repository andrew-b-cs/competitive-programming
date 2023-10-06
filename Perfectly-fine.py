tc = int(input())
for _ in range(tc):
    numBooks = int(input())
    costs = []
    for _ in range(numBooks):
        time, skill = map(str, input().split())
        costs.append([int(time), skill])
        
    costs.sort(key=lambda x:x[0])
    skill1Found = False
    skill2Found = False
    combinedSkillFound = False
    time = 0
    for i in range(len(costs)):
        if (costs[i][1] == "01" and not skill1Found):
            skill1Found = True
            time += costs[i][0]
        if (costs[i][1] == "10" and not skill2Found):
            skill2Found = True
            time += costs[i][0]
        if (costs[i][1] == "11"):
            combinedSkillFound = True
            time = costs[i][0]
        
        if combinedSkillFound:
            print(time)
            skill1Found = True 
            skill2Found = True
            break
        if skill1Found and skill2Found:
            for n in range(i, len(costs)):
                if costs[n][0] > time:
                    break
                if costs[n][1] == "11":
                    time = costs[n][0]
                    break
            skill1Found = True 
            skill2Found = True
            print(time)
            break
            
    if skill1Found == False or skill2Found == False:
        print(-1)
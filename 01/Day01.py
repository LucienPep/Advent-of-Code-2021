with open("SonarData.txt", "r") as rawData:
    sonarData = rawData.readlines()

#Part 1
prevLine = '0'
increaseTotal = 0

for line in sonarData:
    if line > prevLine:
        increaseTotal += 1
    prevLine = line

print(increaseTotal)

#Part 2
prevSet = 0
increaseTotal = 0

for i in range(len(sonarData) - 2 ):
    tempSet = 0
    for x in range(3):
        tempSet += int(sonarData[i + x]) 
    if prevSet != 0 and tempSet > prevSet:
        increaseTotal += 1
    prevSet = tempSet
    

print(increaseTotal)


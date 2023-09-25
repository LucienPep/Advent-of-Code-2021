with open("PositionData.txt", "r") as rawData:
    positionData = rawData.readlines()

horizontal = vertical = depth = 0

for line in positionData:
    movement = int(line.split()[1])
    x = line[0]
    if x == "f": 
        horizontal += movement
        depth += (movement * vertical) 
    elif x == "u":
        vertical -= movement
    else:
        vertical += movement

finalResult = vertical * horizontal
depthResult = depth * horizontal
print(finalResult)
print(depthResult)
with open("PositionData.txt", "r") as rawData:
    positionData = rawData.readlines()

horizontal = vertical = 0

for line in positionData:
    movement = int(line.split()[1])
    x = line[0]
    if x == "f":
        horizontal += movement
    elif x == "u":
        vertical -= movement
    else:
        vertical += movement

finalResult = vertical * horizontal
print(finalResult)
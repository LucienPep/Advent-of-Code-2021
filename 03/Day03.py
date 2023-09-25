with open("BinaryData.txt", "r") as rawData:
    BinaryData = rawData.readlines()

gammaRate = ''
epsilonRate = ''

for i in range(12):
    zero = 0
    one = 0
    for line in BinaryData:   
        if line[i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

print(int(gammaRate,2) * int(epsilonRate,2))

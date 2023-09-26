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

#print(int(gammaRate,2) * int(epsilonRate,2))

#Part2

oxygenRate = ''
co2Rate = ''

for i in range(12):
    oxyZero = oxyOne = co2Zero = co2One = 0
    for line in BinaryData:  
        if oxygenRate[0:i] == line[0:i]:   
            if line[i] == '0':
                oxyZero += 1
            else:
                oxyOne += 1
            
        if co2Rate[0:i] == line[0:i]:   
            if line[i] == '0':
                co2Zero += 1
            else:
                co2One += 1

    if oxyOne == 1 and oxyZero == 0:
        oxygenRate += '1'
    elif oxyOne == 0 and oxyZero == 1:
        oxygenRate += '0'
    elif oxyZero > oxyOne:
        oxygenRate += '0'
    else:
        oxygenRate += '1'
    
    if co2One == 1 and co2Zero == 0:
        co2Rate += "1"
    elif co2One == 0 and co2Zero == 1:
        co2Rate += "0"
    elif co2One > co2Zero:
        co2Rate += "0"
    elif co2One == co2Zero:
        co2Rate += "0"    
    else:
        co2Rate += "1"
    
print(int(oxygenRate,2) * int(co2Rate,2))

#print(oxygenRate)
#print(co2Rate)

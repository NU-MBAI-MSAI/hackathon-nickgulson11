avgTemp = input("Enter the average daily temperature: ")
avgTemp = int(avgTemp)
heatingDays = 0
coolingDays = 0
while avgTemp>-459:
    if avgTemp<60:
        heatingDays += 1
    elif avgTemp>80:
        coolingDays += 1
    avgTemp = input("Enter the average daily temperature: ")
    avgTemp = int(avgTemp)

print("Heating days: " + str(heatingDays))
print("Cooling days: " + str(coolingDays))
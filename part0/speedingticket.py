def speedingTicket(speed, limit):
    difference = speed - limit
    if difference<-10:
        return 50
    elif difference<0:
        return 0
    elif difference>=6 and difference<=20:
        return 75
    elif difference>20 and difference<=40:
        return 150
    elif difference>40:
        return 300


print(speedingTicket(45, 35))
print(speedingTicket(26, 35))
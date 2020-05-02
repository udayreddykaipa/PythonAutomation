r='16911A0'
rolls=[]
for b in range(3,6):
    ro=r+str(b)
    for i in range (1,100):
        if(i<10):
            roll=ro+str(0)+str(i)
        else:
            roll=ro+str(i)
        rolls.append(roll)
    for c in range(65,81):
        if(c==73 or c==79):
            continue
        for i in range(0,10):
            roll=ro+str(chr(c))+str(i)
            rolls.append(roll)
    rolls.append(ro+'Q0')
#done mech.ece.cse

#for eee
ro=r+str(2)
for i in range (1,91):
    if(i<10):
        roll=ro+str(0)+str(i)
    else:
        roll=ro+str(i)
    rolls.append(roll)
#for civil
ro=r+str(1)
for i in range (1,100):
    if(i<10):
        roll=ro+str(0)+str(i)
    else:
        roll=ro+str(i)
    rolls.append(roll)
for c in range(65,68):
    for i in range(0,10):
        roll=ro+str(chr(c))+str(i)
        rolls.append(roll)

#for it
r='16911A1'
ro=r+str(2)
for i in range (1,61):
    if(i<10):
        roll=ro+str(0)+str(i)
    else:
        roll=ro+str(i)
    rolls.append(roll)

    
print(rolls)

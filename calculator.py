print (" ---------------Grade Calculator-------------")
Itilizate = int(input (" Konbyen not ou vle tape? : "))
b = 1
tab=[]
while ( b<=Itilizate):
    val = int(input (" Ekri not ou vle tape? : "))
    tab.append(val)
    b=b+1

s=0
longueur = len(tab)
for i in range(longueur) :
    s=s+tab[i]
    
mwayen = float(s/Itilizate)

if (mwayen >=90) :
    print ("Mwayen lan se ",mwayen ," e li klasifye pa let","A")
elif (mwayen >=80 and mwayen<90):
    print("Mwayen lan se",mwayen ," e li klasifye pa let","B")
elif (mwayen >=70 and mwayen<80):
    print("Mwayen lan se",mwayen ," e li klasifye pa let","C")
elif (mwayen >=60 and mwayen <70):
    print("Mwayen lan se",mwayen ," e li klasifye pa let","D")
else:
    print("Mwayen lan se",mwayen ," e li klasifye pa let","F")

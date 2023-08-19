panye_itilizate = []
def panye (pwodwi, *args):
    panye_itilizate.append(pwodwi)

def pri_total():
    pri_total= 0
    panye = len(panye_itilizate)
    for i in range(panye):
        pri_total= pri_total + panye_itilizate[i]
    print(pri_total)    

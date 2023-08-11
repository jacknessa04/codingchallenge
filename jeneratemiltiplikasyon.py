answer = True
tab = 1
while answer :
    itilizate1 = int(input(" Rantre yon nonb soti nan 1 pou rive nan 10: "))
    test=False
    while (itilizate1 < 1 or itilizate1 >10) :
        itilizate1 = int(input(" Rantre yon nonb soti nan 1 pou rive nan 10: "))
        test=True

    
    while (tab <= 10 and test==False) :
        rezilta = itilizate1 * tab
        print ( f"{tab} * {itilizate1} = {rezilta}")
        tab+= 1
                
    itilizate2 = input (" eskew vle jenere yon lot tab(W|N): ")
        
    if ((itilizate2) == "W" or (itilizate2) == "w"):
        answer = True
        tab =1
    else:
        answer= False
        print ("Bye")

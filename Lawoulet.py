from random import randrange
nonb = randrange(0, 500)

chans = 5
while (chans > 0) :
     nonb_chwazi = int (input("ki nonb wap chwazi? "))
     if (nonb_chwazi== nonb):
         print("felisitasyon! ou genyen, nonb lan se :", nonb)
         break
     elif (nonb_chwazi < nonb) :
            print ("nonb ou chwazi a pi piti. Ou rete:" ,chans-1, "chans")
            chans -=1
     else:
            print ("nonb ou chwazi a pi gran", chans-1, "chans")
            chans -=1
            
if (chans ==0):
       print("dezole ou epuize tout chans ou yo. Nonb lan se : ", nonb)
         
         
    


       
     
     
    

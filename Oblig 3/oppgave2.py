import random

ganger1 = 0
ganger2 = 0
teller = 0
slutter = 0

while(1):
    #her setter vi in random fra 1 til 100 for spiller 1 og 2
    spiller1 = random.randrange(1, 100)
    spiller2 = random.randrange(1, 100)

    ganger1 = ganger1 + spiller1
    ganger2 = ganger2 + spiller2
    teller = teller + 1


    print("summen av spiller 1 etter runde %d er : %d"%(teller, ganger1))
    #her sier vi hvor lang spille skal være vi
    if(ganger1>=200):
        slutter=1
        break
    print("summen av spiller 2 etter runde %d er : %d"%(teller, ganger2))
    if(ganger2>=200):
        slutter=2
        break
 #når en spiller vinner så print ut vinner.
if(slutter==1):
    print("spiller 1 vant")
else:
    print("spiller 2 vant")


import random
#import secrets
import turtle
print("choose your level : a) easy b) medium c) hard")
level=str(input())
#choisis un mot au hazard dans la liste "mot"
mota=["temps","route","fleur","coeur", "porte", "kayak", "bisou","bombe","ecrin","jeune","archer"]
motb=["peinture","octogone","moccassin"]
motc=["superstition","accrobranche",  "reminiscence", "architecture","consentement","sinusoidales"]

if level=="a":
    random_index = random.randint(0,len(mota)-1)
    motchoisi = mota[random_index]
if level=="b":
    random_index = random.randint(0,len(motb)-1)
    motchoisi = motb[random_index]
if level=="c":
    random_index = random.randint(0,len(motc)-1)
    motchoisi = motc[random_index]
motsecret=[]
mottirret=[]
i=0
for i in range (0,len(motchoisi)):
    motsecret.append(motchoisi[i])
i=0
for i in range (len(motsecret)):
    mottirret.append('-')
print("mot ici", mottirret)

erreur=0
valide=0
lettreu = []

while(erreur<6 and valide<len(motsecret)):
    l=1
    print("Donnez une lettre.")
    lettre=str(input())
    if lettre not in lettreu :
        for f in range(0,len(motsecret)):
            n=1+f
        
            if lettre==motsecret[f] :
                print(motsecret[f],n, "eme lettre")
                mottirret[f]=lettre
                print (mottirret)
                valide=valide+1
                l=2
    else :
        print ("cette lettre a déjà été donnée")
        l=2
           
    if l==1 :
        print("cette lettre ne fait pas partie du mot")
        erreur= erreur+1
        if erreur==1 :
            turtle.setup(700, 1000)
            turtle.color("black")
            turtle.up()
            turtle.goto(-100,-400)
            turtle.down()
            turtle.goto(-150,-400)
            turtle.goto(-125,-400)
            turtle.goto(-125,25)
            turtle.goto(0,25)
            turtle.goto(0,0)
            turtle.up()
            turtle.goto(0,-100)
            turtle.down()
        if erreur==2:
                ##cercle de 200 pixels de rayon
            turtle.circle(50)
            turtle.up()
        if erreur==3:
                ##cercle de 200 pixels de rayon
            turtle.goto(25,-55)
            turtle.down()
            turtle.goto(5,-30)
            turtle.up()
            turtle.goto(5,-50)
            turtle.down()
            turtle.goto(25,-30)
            turtle.up()
            turtle.goto(-25,-55)
            turtle.down()
            turtle.goto(-5,-30)
            turtle.up()
            turtle.goto(-5,-50)
            turtle.down()
            turtle.goto(-25,-30)
            turtle.up()
        if erreur==4:
                ##bras
            turtle.goto(0,-100)
            turtle.down()
            turtle.goto(-75,-175)
            turtle.up()
            turtle.goto(0,-100)
            turtle.down()
            turtle.goto(75,-175)
            turtle.up()
        if erreur==5:
            ##corp
            turtle.up()
            turtle.goto(0,-100)
            turtle.down()
            turtle.goto(0,-250)
            turtle.up()

    if l==2 :
        lettreu.append(lettre)
    
    
if valide==len(motsecret) :
    print("bravo le mot était", motchoisi)

if erreur==6 : 
    print ("pas de chance, le mot était", motchoisi)
        ##jambes
    turtle.goto(0,-250)
    turtle.down()
    turtle.goto(-75,-325)
    turtle.up()
    turtle.goto(0,-250)
    turtle.down()
    turtle.goto(75,-325)
    turtle.up()
    turtle.exitonclick()
    





    # il se passe ça quand on apprend, on sait faire les trucs beaucoup mieux, 
    # donc tout ce qui reste ici est absoluement innutile et à été remplacé par une dizaine de ligne...
    '''if level=="b":
    mot=["peinture","octogone","moccassin"]
    random_index = random.randint(0,len(mot)-1)
    motchoisi=mot[random_index]
    motsecret=[]
    mottirret=['-','-','-','-','-','-','-','-']
    i=0
    for i in range (0,8):
        motsecret.append(motchoisi[i])
    erreur=0
    valide=0
    lettreu = []

    while(erreur<10 and valide<8):
        l=1
        
        print("Donnez une lettre.")
        lettre=str(input())
        if lettre not in lettreu :
            for f in range(0,len(motsecret)):
                n=1+f
                if lettre==motsecret[f] :
                    print(motsecret[f],n, "eme lettre")
                    mottirret[f]=lettre
                    print (mottirret)
                    valide=valide+1
                    l=2
        else :
            print ("cette lettre a déjà été donnée")
            l=2
        
        
                
        if l==1 :
            print("cette lettre ne fait pas partie du mot")
            erreur= erreur+1
            if erreur==1 :
                turtle.setup(700, 1000)
                turtle.color("black")
                turtle.up()
                turtle.goto(-100,-400)
                turtle.down()
                turtle.goto(-150,-400)
                turtle.goto(-125,-400)
            if erreur==2:
                turtle.goto(-125,25)
                turtle.goto(0,25)
                turtle.goto(0,0)
                turtle.up()
                turtle.goto(0,-100)
                turtle.down()
            if erreur==3:
                    ##cercle de 200 pixels de rayon
                turtle.circle(50)
                turtle.up()
            if erreur==4:
                    ##cercle de 200 pixels de rayon
                turtle.goto(25,-55)
                turtle.down()
                turtle.goto(5,-30)
                turtle.up()
                turtle.goto(5,-50)
                turtle.down()
                turtle.goto(25,-30)
                turtle.up()
            if erreur==5:
                turtle.goto(-25,-55)
                turtle.down()
                turtle.goto(-5,-30)
                turtle.up()
                turtle.goto(-5,-50)
                turtle.down()
                turtle.goto(-25,-30)
                turtle.up()
            if erreur==6:
                    ##bras
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(-75,-175)
                turtle.up()
            if erreur==7:
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(75,-175)
                turtle.up()
            if erreur==8:
                ##corp
                turtle.up()
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(0,-250)
                turtle.up()
            
            if erreur==9:
                turtle.goto(0,-250)
                turtle.down()
                turtle.goto(-75,-325)
                turtle.up()
        if l==2 :
            lettreu.append(lettre)
        
    if valide==8 :
        print("bravo le mot était", motchoisi)
    if erreur==10 : 
        print ("pas de chance, le mot était", motchoisi)
        turtle.goto(0,-250)
        turtle.down()
        turtle.goto(75,-325)
        turtle.up()
        turtle.exitonclick()

if level=="c":
    mot=["superstition","accrobranche",  "reminiscence", "architecture","consentement","sinusoidales"]
    random_index = random.randint(0,len(mot)-1)
    motchoisi=mot[random_index]
    motsecret=[]
    mottirret=['-','-','-','-','-','-','-','-','-','-','-','-']
    i=0
    for i in range (0,12):
        motsecret.append(motchoisi[i])
    erreur=0
    valide=0
    lettreu = []

    while(erreur<13 and valide<12):
        l=1
        print("Donnez une lettre.")
        lettre=str(input())
        if lettre not in lettreu :
            for f in range(0,len(motsecret)):
                n=1+f
                if lettre==motsecret[f] :
                    print(motsecret[f],n, "eme lettre")
                    mottirret[f]=lettre
                    print (mottirret)
                    valide=valide+1
                    l=2
        else :
            print ("cette lettre a déjà été donnée")
            l=2
        
        
                
        if l==1 :
            print("cette lettre ne fait pas partie du mot")
            erreur= erreur+1
            if erreur==1 :
                turtle.setup(700, 1000)
                turtle.color("black")
                turtle.up()
                turtle.goto(-100,-400)
                turtle.down()
                turtle.goto(-150,-400)
                turtle.goto(-125,-400)
            if erreur==2:
                turtle.goto(-125,25)
            if erreur==3:
                turtle.goto(0,25)
                turtle.goto(0,0)
                turtle.up()
                turtle.goto(0,-100)
                turtle.down()
            if erreur==4:
                    ##cercle de 200 pixels de rayon
                turtle.circle(50)
                turtle.up()
            if erreur==5:
                    ##cercle de 200 pixels de rayon
                turtle.goto(25,-55)
                turtle.down()
                turtle.goto(5,-30)
                turtle.up()
            if erreur==6:
                turtle.goto(5,-50)
                turtle.down()
                turtle.goto(25,-30)
                turtle.up()
            if erreur==7:
                turtle.goto(-25,-55)
                turtle.down()
                turtle.goto(-5,-30)
                turtle.up()
            if erreur==8:
                turtle.goto(-5,-50)
                turtle.down()
                turtle.goto(-25,-30)
                turtle.up()
            if erreur==9:
                    ##bras
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(-75,-175)
                turtle.up()
            if erreur==10:
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(75,-175)
                turtle.up()
            if erreur==11:
                ##corp
                turtle.up()
                turtle.goto(0,-100)
                turtle.down()
                turtle.goto(0,-250)
                turtle.up()
            
            if erreur==12:
                turtle.goto(0,-250)
                turtle.down()
                turtle.goto(-75,-325)
                turtle.up()
        if l==2 :
            lettreu.append(lettre)
        
    if valide==12 :
        print("bravo le mot était", motchoisi)
    if erreur==13 : 
        print ("pas de chance, le mot était", motchoisi)
        turtle.goto(0,-250)
        turtle.down()
        turtle.goto(75,-325)
        turtle.up()
        turtle.exitonclick()
    '''
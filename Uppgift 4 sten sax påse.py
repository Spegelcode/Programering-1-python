import random # Här impoterar vi in random elementet till programet
ditt_val = input("sten, sax eller påse? ") #här får bi input från spelaren från de möjliga valen
val = ("sten", "sax", "påse") # Här gör vi en lista med möljliga val
datorn_val = random.choice(val) #här väljer datorn med hjälp av import random från listan val
print(f"Datorns val {datorn_val}. ")# skriver ut datorns val
if ditt_val == datorn_val: # >Här kollar vi ifall datorn och användaren har valt samma val från listan
    print("Det blev oavgjort!")# Skriver ut resultat
elif (ditt_val == "sten" and datorn_val == "sax") or (ditt_val == "sax" and datorn_val == "påse") or (ditt_val == "påse" and datorn_val == "sten"):#Här är alla vinst givande resultat
    print("Du vann")#skriver ut "Du vann" ifall vi fick ett av resultaten från från linjen över
else: print("Du förlorade")#Här skriver vi ut "Du förlorade" som en defult ifall inget av de andra resultaten uppnåtts 
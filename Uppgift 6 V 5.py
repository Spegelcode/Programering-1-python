a1 = 0 #Män
g1 = 0 # Mäns samanlagda ålder
a2 = 0 # Antal kvinnor
g2 = 0 # Kvinnors samanlagda ålder


# Få andvändaren att skriva in ålder och kön
ålder = int(input("Skriv in din ålder: "))
kön = input("Är du man eller kvinna: ")
#kategoriserar man/ålder och kvinna/ålder
if kön == "man": #Kollar ifall input matchar kategori a1
    a1 += 1 # lägger till 1 man i a1 
    g1 += ålder #lägger input man ålder till g1

elif kön == "kvinna":
    a2 += 1 # Lägger till 1 kvinna till a2 
    g2 += ålder #lägger till kvinna ålder till g2 

else: 
    print("Invalid input")    
    
#Frågar ifall andvändaren vill lägga till fler personer
while True: 
    fler = input("Vill du lägga till flera personer? y/n: ")
    if fler == "y":   
        ålder = int(input("Skriv in din ålder: "))
        kön = input("Är du man eller kvinna: ")

        if kön == "man": #Kollar ifall input matchar kategori a1
            a1 += 1 # lägger till 1 man i a1 
            g1 += ålder  #lägger input man ålder till g1
        elif kön == "kvinna":
            a2 += 1 # Lägger till 1 kvinna till a2 
            g2 += ålder #lägger till kvinna ålder till g2 

        else: # Skriver ut invalid input ifall något annat än de givna altenativen skrivs in
            print("Invalid input")    
    else:
       
#räknar ihop genomsnitt ifall minst en av varje kön lagts in
     if  a1 > 0 and a2 > 0:
        m1 = g1 / a1 #beräknar genomsnittet för män
        m2 = g2 / a2 # Beräknar genomsnittet för kvinnor 
    #Skriver ut resultatet 
        print("Genomsnitts åldern för", a1, "man", m1)
        print("Genomsnitts åldern för", a2, "kvinnor är", m2)
     else: #skriver ut ett error medelande ifall du inte lagt in två kön
        print("Vänligen skriv in minst en man och en kvinna ")
        break #avslutar och skriver ut resultal
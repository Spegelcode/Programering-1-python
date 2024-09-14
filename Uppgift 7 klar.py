# Den här koden räknar ut vilken skatt du kommer behöva betala efter du skriver in ditt årsinkomst. 
# Här delar vi upp de olika skatte sicken 
övre = 638500 # Det högsta skatten 25 %
nedre = 438900 # Normal skatt 20%
grund = 13100 # Skattefri inkomst 0 %

# samlar in ett värde, kategoriserar det och sedan ger oss en % av det i värde
while True: # while true är en loop som loopar koden 
    
    try:
        årsinkomst = int(input("Skriv in din årsinkomst: ")) #Vi ber om input från användaren i int dvs siffror
    except:
        print("Vänligen skriv in med siffror") # Ifall användaren inte skriver in sifron skriver vi ut medelandet 
        continue # Vi fortsätter loopen
    
    
    if årsinkomst <= grund: # kollar om inkomsten är lägre är grund värdet
        print("Du behöver inte betala skatt") #Skriver ut stingen ifall if kraven möts
    
    elif årsinkomst >= grund and årsinkomst <= övre: # Kollar ifall input värdet är större övre än eller mindre än grund
        statlig_skatt = årsinkomst * 0.2 # räknar ut skatten 20 %
        print("Din skatt är", statlig_skatt, "kr") # Skriver ut skatten av 20 % av inkomsten
    
    elif årsinkomst >= övre: # kollar ifall input värdet är högre än övre (638500) 
        statlig_skatt = årsinkomst * 0.25 # Tar värdet och multiplicerar det med 0.25 (25 % skatt satsen) för att få ut skatt
        print("Din skatt är", statlig_skatt, "kr") # Skriver ut skatten av 25 % av inkomsten

        

    ny_inkomst = input("Vill du beräkna en till skatt ? (ja/nej?) ") #Frågar ifall användaren vill beräkna en till inkomstskatt
    if ny_inkomst.lower() != "ja" and ny_inkomst.lower() != "Ja": # Kollar ifall svaret inte är Ja eller ja  
        break #avslutar loopen och kör då om loopen från while true
print("Programmet avslutas") # Skriver ut programmet avslutas ifall svaret inte är Ja eller ja på rad 29
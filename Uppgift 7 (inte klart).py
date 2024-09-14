# Den här koden räknar ut vilken skattt du kommer behöva betala efter du skriver in ditt årsinkomst. 
# Här delar vi upp de olika skattesicken 
övre = 638500 # Det högsta skatten
nedre = 438900 # Grundskatt
grund = 13100 # Skattefri inkomst

# sammlar in ett värde, kategoriserar det och sedan ger oss en % av det i värde
while True: # while true är en loop som loopar koden 
    
    try:
        årsinkomst = int(input("Skriv in din årsinkomst: ")) #Vi ber om input från användaren i int dvs siffror
    except:
        print("Vänligen skriv in med siffror") # Ifall användaren inte skriver in siffron skriver vi ut medelandet 
        continue # Vi fortsätter loopen
    
    
    if årsinkomst <= grund: # kollar om inkomsten är lägere är grund värdet
        print("Du behöver inte betala skatt") #Skriver ut stingen ifall if kraven möts
    
    elif årsinkomst >= grund and årsinkomst <= övre: # Kollar ifall input värdet är större övre än eller mindre än grund
        statlig_skatt = årsinkomst * 0.2 # räknar ut skatten 20 %
        print("Din skatt är", statlig_skatt, "kr") # Skriver ut skatten av 20 % av inkomsten
    
    elif årsinkomst >= övre: # kollar ifall input värdet är högere än övre (638500) 
        statlig_skatt = årsinkomst * 0.25 # Tar värdet och gångrar det med 0.25 (25 % skatt sattsen) för att få ut skatt
        print("Din skatt är", statlig_skatt, "kr") # Skriver ut skatten av 25 % av inkomsten

        

    ny_inkomst = input("Vill du beräkna en till skatt ? (ja/nej?) ") #Frågar ifall användaren vill beräkna en till inkomstskatt
    if ny_inkomst.lower() != "ja" and ny_inkomst.lower() != "Ja": # Kollar ifall svaret är inte är Ja eller ja  
        break #avslutar loopen och kör då om loopen från while true
print("Programet avslutas") # Skriver ut programet avslutas ifall svaret inte är Ja eller ja på rad 29

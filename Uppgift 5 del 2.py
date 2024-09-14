minstring ='1966grundade456for789data'# En variabel med en sträng med ord och siffror
summa = 0 # En variabel med värdet 0
heltal = "" # En variabel med värdet ""
for tecken in minstring: # en for loop som loopar genom tecken i minstring
    if tecken.isnumeric(): # Vi kollar numeriska tecken i minstring
        heltal += tecken # sammlar in heltalen till heltal
    elif heltal: # 
        summa += int(heltal)#sumerar och l'ggs till i summa
        heltal = ""# heltal blir en tom sträng
if heltal:#kollar ifall det finns sifror kvar i heltal
    summa += int(heltal) #om det finns kvar lägger till det i summa
    
print(summa) #skriver ut summa
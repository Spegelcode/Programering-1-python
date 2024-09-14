input_string = input("hej, vänligen skriv en mening med twå eller fler ord. ") #Här ber vi användaren att skrivva in en mening
response = input_string.split()#Här tar vi den meningen och delar upp den i ord
num_response = len(response)#här räknar vi ut hur många ord det är 
print("Du skrev", num_response, "ord.")#Här tar vi datan och skriver ut hur många ord med hjälp av num
print("Det första ordet är:", response[0])#Här tar vi ut det första ordet i stringen och skriver ut det från listan
print("Det sista ordet är:", response[-1])#Här tar vi ut det sista ordet i stringen och skriver ut det från listan
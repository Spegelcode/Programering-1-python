#v ett program som beräknar volymen och arean av en sfär med hjälp av Math funktion. Sfärens radie ska läsas in från kommandofönstret. 
#Volymen av en sfär kan beräknas med följande formel: V= (4⋅π⋅r^3)/3. Använd math modul!

import math # här impoterar vi math

sfären = float(input("Skriv in sfärens radie: ")) # Här får vi in användarens radie 
sfären_area = 4 * math.pi * sfären**2 #Här räknar vi ut area
sfärens_volym = 4 * math.pi * sfären/3  #Här räknar vi ut volymen
print("sfären area:", sfären_area) # skriver ut area
print("sfärens volym:", sfärens_volym) # skriver ut volymen
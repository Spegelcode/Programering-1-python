import math #importerar math

sum = 0.0 #Sätter sum till 0.0 
err = 1e-5 #tilldelar värde till err
k = 1 # k tilldelas värdet 1

while abs(math.pi - 4 * sum) > err: # beräknar med abs för att nå  nära pi
    sum += math.pow(-1, k + 1) / (2 * k - 1) # leibniz formeln
    k += 1 # ökar värdet av k med 1 
    
print("Iteration", k, "pi = ", 4 * sum, "err = ", abs(math.pi - 4 * sum))  # skriver ut resultatet

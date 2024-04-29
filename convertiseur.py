#x =float(input("choisir un nombre décimal? "))
#y = (x - 32) * 5/9
#print(str(y) + "°C" )

#x = input("quel devise voulez- vous convertir? ")
#y = float(input("quel montant à convertir? " ))
#z = input("vers quel devise? ")
#if x =="Dollars" :
#    if z =="Euro" :
#        M = y*(0.93)
#        print("le montant en euro est: "+str(M)+" euros")
#elif x =="Dirham marocain" :
#    if z == "Euro" :
#        M = y*(0.092)
#        print("Le montant en euro est:"+ str(M))
        
#a = int(input("Combien d'heures se sont écoulées? "))
#b = int(input("Combien de minites se sont écoulées? "))
#c = int(input("Combien de secondes se sont écoulées? "))
#R = a*60*60 + b*60 + c
#print(R)

T = int(input("Combien de secondes se seont écoulées? "))
H = T//3600

m = T - (H*3600)
M = m//60

S = m - (M * 60)
print("Cela fait: "+str(H)+" heures",str(M)+" minutes "+" et "+ str(S)+ " secondes")



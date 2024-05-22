

s=0

A =int(input("Quel est le nom du chien de Tintin? "+"\n voulez-vous 2 ou 4 choix"))
if A == 2 :
    a =input("Milou ou Jacques Chirac?")
    
    if a == "Milou" :
        print("Félicitations, c'est la bonne réponse, vous gagner un point")
        s=s+1    
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
else :
    b = input("Jacques, Milou , Belle ou Chien")
    if b =="Milou" :
        print("Félicitations, c'est la bonne réponse, vous gagner deux point")
        s=s+2
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
B = int(input("quelle est la capitale de la Norvège" + "\n voulez vous 2 ou 4 choix? "))
if B ==2 :
    a = input("Bruxelles ou Oslo? ")
    if a == "Oslo" :
        print("Félicitations, c'est la bonne réponse, vous gagner un point")
        s=s+1
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
else :
    b = input("Rabat, Paris, Oslo ou Madrid? ")
    if b == "Oslo" :
        print("Félicitations, c'est la bonne réponse, vous gagner deux point")
        s=s+2
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
        
C = int(input("Combien de cotés égaux à un triangle isocèle? "+"\n voulez-vous 2 ou 4 choix? "))
if C ==2 :
    a = input("deux ou trois")
    if a =="deux" :
        print("Félicitations, c'est la bonne réponse, vous gagner un point")
        s=s+1
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
else :        
    b = input("zéro, un, deux ou trois")
    if b=="deux" :
        print("Félicitations, c'est la bonne réponse, vous gagner deux point")
        s=s+2
    else :
        print("Incorrect, vous ne remporter pas de points")
        s=s+0
        
D = int(input("quelle est la racine carré de 9? "))
if D == 3 :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
    c=input("voulez-vous 2 ou 4 choix")
    if c ==2 :
        cc =input("1 ou 3? ")
        if cc ==3 :
           print("Félicitations, c'est la bonne réponse, vous gagner un point")
           s=s+1
        else :
           print("Incorrect, vous ne remporter pas de points")
           i=0
    else :
         ccc=input("1, 2, 3, 4? ")
         if ccc == 3 :
             print("Félicitations, c'est la bonne réponse, vous gagner deux point")
             s=s+2
         else :
             print("Incorrect, vous ne remporter pas de points")
             s=s+0
         
E = input("Quel est le plus long fleuve au monde? ")
if E == "Amazone" :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
    print("Incorrect, vous ne remporter pas de points")
    s=s+0
    
F = input("Quel est le plus haut sommet au monde? ")
if F =="Everest" :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    i=3
else :
    print("Incorrect, vous ne remporter pas de points")
    i=0
    
G = input("Quelle langue on parle au Brésil? ")
if G =="Portugais" :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
    print("Incorrect, vous ne remporter pas de points")
    s=s+0
    
H = input("quel animal le plus rapide au monde? ")
if H=="Guépard" :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
    h = int(input("voulez-vous 2 ou 4 choix? "))
    if h ==2 :
        hh= input("Guépard ou cheval? ")
        if hh==H :
            print("Félicitations, c'est la bonne réponse, vous gagner un point")
            s=s+1
    else :
        hhh= input("Cheval, Lièvre, Guépard ou Puma? ")
        if hhh==H :
            print("Félicitations, c'est la bonne réponse, vous gagner deux point")
            s=s+2
        else :
            print("Incorrect, vous ne remporter pas de points")
            s=s+0

I = int(input("quelle année la révolition Française? "))
if I ==1789 :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
     print("Incorrect, vous ne remporter pas de points")
     s=s+0
     
J = input("Quel est le pays du soleil levant? ")
if J =="Japon" :
    print("Félicitations, c'est la bonne réponse, vous gagner trois point")
    s=s+3
else :
    print("Incorrect, vous ne remporter pas de points")
    s=s+0
print("Votre score est: "+str(s))

if s>= 21:
    Q = input("Combien de personnes ont répondu tout juste? ")
    if Q = 100 :
        print("Vous etes le grand gagnant de ce Quiz!")
    else:
        print("Vous pouvez retentez votre chance une autre fois!")
    

    

            
            
            
            
            
            
    


    
    
    
    
    
    
            
            
        
            
            
            

import random

sommeJoueur = 100
a=sommeJoueur
while a>0:
    
    pari = int(input("Combien d'argent voulez-vous parier? "))
    a=a-pari
    if pari > sommeJoueur:
        print("stop! Vous n'avez pas assez d'argent! Pour continuer, vous devez miser à nouveau")

    else:

        A = input("souhaitez-vous parier sur un nombre exact ou sur pair/impair? ")
        I = random.randint(1,36)
        if A== "un nombre exact":
            AA=int(input("choisis un nombre entre 1 et 36? "))
            if AA != I :
                sommeJoueur = 100 - pari
                print("il vous reste"+ str(sommeJoueur)+" euro"+" à jouer")
            else:
                sommeJoueur = 36* pari
                print("wow vous avez maintenant"+str(sommeJoueur)+" euro")
        else :
            BB = input("Choisis pair ou impair")
            if BB == "pair" :
                if I %2 == 0:
                    sommeJoueur = 2*pari
                    print("Wow! Vous avez "+str(sommeJoueur)+ "euro")
                else :
                    sommeJoueur = 100 - pari
                    print("Il vous reste "+str(sommeJoueur)+"euro")
            else :
                if (I+1) %2 == 0:
                    sommeJoueur = 2*pari
                    print("Wow! Vous avez "+str(sommeJoueur)+ "euro")
                else :
                    sommeJoueur = 100 - pari
                    print("Il vous reste "+str(sommeJoueur)+"euro")
                
            
            
            
           
    


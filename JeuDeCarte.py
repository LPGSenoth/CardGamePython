import random, Carte

class JeuDeCartes:
    couleurs = ('coeur', 'pique', 'carreau', 'trefle')
    valeurs = ('7', '8', '9', '10', 'V', 'D', 'R', 'AS')

    def __init__(self):
        self.cartes = [Carte.Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs]
        #print (len(self.cartes))
        
    def shuffling(self):
        #print (len(self.cartes))
        for _ in range(1000):
            i = random.randint(0, len(self.cartes)-1)
            j = random.randint(0, len(self.cartes)-1)
            #print(f"Indices échangés: {i}, {j}")
            self.cartes[i], self.cartes[j] = self.cartes[j], self.cartes[i]

    def enleve_carte(self, carte):
        self.cartes.remove(carte)
        
    def __str__(self):
        #La méthode join prend une liste en paramètre et regroupe ses éléments en une seule chaîne de caractères, séparée par la chaîne sur laquelle join est appelée
        return ', '.join(str(carte) for carte in self.cartes)

            

#J = JeuDeCartes()
#print(J)

#c = Carte.Carte('V', 'coeur')
#J.enleve_carte(c)
#print(J)

#J.shuffling()
#print(J)
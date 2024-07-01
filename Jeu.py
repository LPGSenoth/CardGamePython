import Joueur

class Jeu:
    def __init__(self, joueur1, joueur2, arbitre):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.arbitre = arbitre
        self.vainqueur = None
        
    def imprimer_jeu_de_cartes(self):
        print(f"Jeu de cartes de {self.joueur1.nom}:")
        print(self.joueur1.cartes)
        print(f"Jeu de cartes de {self.joueur2.nom}:")
        print(self.joueur2.cartes)
        
    def comparer_cartes(self, carte1, carte2):
        valeurs = {'7': 0, '8': 1, '9': 2, '10': 3, 'V': 4, 'D': 5, 'R': 6, 'AS': 7}
        return (valeurs[carte1.valeur] > valeurs[carte2.valeur]) - (valeurs[carte1.valeur] < valeurs[carte2.valeur])
    # Si carte1 est plus forte que carte2 : = 1
    # Si carte2 est plus forte que carte1 : = -1
    # Si carte1 est égale à carte2 : = 0

    def simuler_jeu(self):
        for _ in range(32):
            if not self.joueur1.cartes.cartes or not self.joueur2.cartes.cartes:
                break
            carte1 = self.joueur1.cartes.cartes[0]
            carte2 = self.joueur2.cartes.cartes[0]
            self.joueur1.cartes.enleve_carte(carte1)
            self.joueur2.cartes.enleve_carte(carte2)
            comparaison = self.comparer_cartes(carte1, carte2)
            if comparaison > 0:
                self.joueur1.points += 1
            elif comparaison < 0:
                self.joueur2.points += 1
            else:
                self.arbitre.points += 5

    def mettre_a_jour_vainqueur(self):
        if self.arbitre.points > self.joueur1.points and self.arbitre.points > self.joueur2.points:
            self.vainqueur = self.arbitre
        elif self.joueur1.points > self.joueur2.points:
            self.vainqueur = self.joueur1
        elif self.joueur2.points > self.joueur1.points:
            self.vainqueur = self.joueur2
        else:
            self.vainqueur = self.arbitre

    def donner_resultats(self):
        print("Résultats du jeu:")
        print(f"{self.joueur1.nom}: {self.joueur1.points} points")
        print(f"{self.joueur2.nom}: {self.joueur2.points} points")
        print(f"Arbitre: {self.arbitre.points} points")
        if isinstance(self.vainqueur, Joueur.Joueur):  # Vérifie si le vainqueur est une instance de Joueur
            print(f"Le vainqueur est {self.vainqueur.nom}")
        elif isinstance(self.vainqueur, Joueur.Arbitre):  # Vérifie si le vainqueur est une instance d'Arbitre
            print("Le vainqueur est l'arbitre")
        else:
            print("Erreur: Vainqueur inconnu")
            
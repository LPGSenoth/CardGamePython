from JeuDeCarte import JeuDeCartes



class Personne :
    def __init__(self,nom,points= 0, nombre_parties_gagnees = 0):
        self.nom = nom
        self.points = points
        self.nombre_parties_gagnees = nombre_parties_gagnees


class Joueur(Personne):
    def __init__(self,nom,points = 0,nombre_parties_gagnees = 0,cartes = None):
        Personne.__init__(self, nom,points,nombre_parties_gagnees)
        self.cartes = cartes

    def __str__(self):
        return f"le joueur sappelle {self.nom}"


class Arbitre(Personne):
    def __init__(self,nom,points=0,nombre_parties_gagnees=0):
        Personne.__init__(self, nom, points, nombre_parties_gagnees)

    def __str__(self):
        return f"l'arbitre s'appelle {self.nom}"


    def donne_cartes_melangees_joueur(self,Joueur):
        Joueur.cartes = JeuDeCartes()
        Joueur.cartes.shuffling()
        return Joueur.cartes

        

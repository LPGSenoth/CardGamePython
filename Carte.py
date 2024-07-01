class Carte:
    def __init__(self, valeur, couleur):
        self.couleur = couleur
        self.valeur = valeur
    
    def __str__(self):
        return f"{self.valeur}_{self.couleur}"
    
    def __eq__(self, o_card: object) -> bool:
        return self.valeur == o_card.valeur and self.couleur == o_card.couleur

    def __gt__(self, o_card: object) -> bool:
        return self.valeur > o_card.valeur
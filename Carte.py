class Carte:
    def __init__(self, valeur, couleur):
        self.couleur = couleur
        self.valeur = valeur
        self.card_values = {"7": 7, "8": 8, "9": 9,"10": 10, "V": 11, "D": 12, "R": 13, "AS": 14}
        self.card_colors = {"Coeur": 4, "Pique": 3, "Carreau": 2, "Trefle": 1}
    
    def __str__(self):
        return f"{self.valeur}_{self.couleur}"
    
    def __eq__(self, o_card: object) -> bool:
        return self.valeur == o_card.valeur and self.couleur == o_card.couleur

    def __gt__(self, o_card: object) -> bool:
        return (False if (self == o_card) else (True if (self.valeur == o_card.valeur and self.card_colors[self.couleur] > o_card.card_colors[o_card.couleur]) else (True if self.card_values[self.valeur] > self.card_values[o_card.valeur] else False)))
    

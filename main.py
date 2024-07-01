from Jeu import Jeu
from Joueur import Joueur, Arbitre

# Create players and referee
toto = Joueur('toto')
titi = Joueur('titi')
donald = Arbitre('donald')

# Function to run 100 simulations
def run_simulations():
    historique = []
    toto_victoires = 0
    titi_victoires = 0
    donald_victoires = 0

    for i in range(1, 101):
        # Reset points for each new game
        toto.points = 0
        titi.points = 0
        donald.points = 0

        # Shuffle and deal cards
        donald.donne_cartes_melangees_joueur(toto)
        donald.donne_cartes_melangees_joueur(titi)

        # Create and simulate game
        partie = Jeu(joueur1=toto, joueur2=titi, arbitre=donald)
        partie.simuler_jeu()
        partie.mettre_a_jour_vainqueur()
        
        # Collect results
        if isinstance(partie.vainqueur, Joueur):
            vainqueur_nom = partie.vainqueur.nom
            if partie.vainqueur == toto:
                toto_victoires += 1
            else:
                titi_victoires += 1
        else:
            vainqueur_nom = "l'arbitre s'appelle donald"
            donald_victoires += 1

        resultat = f"partie {i} : {toto.nom} a eu {toto.points} points, {titi.nom} a eu {titi.points} points, donald a eu {donald.points} points, le vainqueur est {vainqueur_nom}\n"
        historique.append(resultat)

    # Write to file
    with open("historique_jeux.txt", "w", encoding="utf-8") as f:
        f.writelines(historique)
        f.write(f"\ntoto a gagné {toto_victoires} parties\n")
        f.write(f"titi a gagné {titi_victoires} parties\n")
        f.write(f"donald a arbitré {donald_victoires} parties\n")

# Run the simulations
run_simulations()
import Jeu, Joueur

toto = Joueur.Joueur('Toto')
titi = Joueur.Joueur('Titi')
donald = Joueur.Arbitre('Donald')
donald.donne_cartes_melangees_joueur(toto)
donald.donne_cartes_melangees_joueur(titi)
partie = Jeu.Jeu(joueur1=toto, joueur2=titi, arbitre=donald)
partie.imprimer_jeu_de_cartes()
partie.simuler_jeu()
partie.mettre_a_jour_vainqueur()
partie.donner_resultats()
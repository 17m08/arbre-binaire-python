from modules_arbres import *

racine=Noeud("A", Noeud("B", Noeud("C", None, Noeud("E")), Noeud("D")), Noeud("F"))
arbre=Arbre(racine)
dessiner(arbre)
# Executer ce que vous voulez comme l'affichage de la hauteur, la taille, etc...

# Représentation d'arbres binaires – Python

Un moyen simple et pédagogique de représenter et manipuler des arbres binaires en Python.  
Ce projet est destiné à un usage **personnel ou éducatif**, notamment pour comprendre les concepts fondamentaux liés aux arbres.

---

## ⚙️ Objets

- `Noeud` : représente un nœud de l’arbre  
  - `valeur` : valeur stockée dans le nœud  
  - `gauche` : sous-arbre gauche  
  - `droite` : sous-arbre droit  

- `Arbre` : représente un arbre binaire et contient l’ensemble des méthodes de manipulation et d’analyse

---

## 🧑‍🏫 Méthodes

### Structure et propriétés
- `est_vide()`  
  → Vérifie si l’arbre est vide.

- `taille()` / `nb_noeuds()`  
  → Retourne le nombre total de nœuds de l’arbre.

- `hauteur()`  
  → Calcule la hauteur de l’arbre.

- `nb_feuilles()`  
  → Retourne le nombre de feuilles (nœuds sans enfants).

- `est_feuille()`  
  → Vérifie si la racine est une feuille.

---

### Parcours de l’arbre
- `parcours_prefixe()`  
  → Parcours **préfixe** (racine, gauche, droite).

- `parcours_infixe()`  
  → Parcours **infixe** (gauche, racine, droite).

- `parcours_postfixe()`  
  → Parcours **postfixe** (gauche, droite, racine).

- `parcours_largeur()`  
  → Parcours en **largeur** (niveau par niveau).

---

### Recherche et insertion
- `rechercher(valeur)`  
  → Recherche une valeur dans l’arbre.

- `inserer_bts(valeur)`  
  → Insère une valeur dans un **arbre binaire de recherche (BST)**.

---

### Propriétés avancées
- `est_binaire()`  
  → Vérifie que chaque nœud possède au maximum deux enfants.

- `est_complet()`  
  → Vérifie si l’arbre est **complet**.

- `est_parfait()`  
  → Vérifie si l’arbre est **parfait** (toutes les feuilles au même niveau).

- `est_equilibre()`  
  → Vérifie si l’arbre est **équilibré** (différence de hauteur ≤ 1).

---

### Affichage
- `dessiner()`  
  → Affiche l’arbre dans la console sous forme ASCII pour une meilleure visualisation.

---

## 📌 Exemple d’utilisation

```python
from modules_arbres import *

racine=Noeud("A", Noeud("B", Noeud("C", None, Noeud("E")), Noeud("D")), Noeud("F"))
arbre=Arbre(racine)
dessiner(arbre)
print("Hauteur :", arbre.hauteur())
print("Taille :", arbre.taille())
# et un de suite de suite
```

## 🎯 Objectif du projet

- Comprendre la structure des arbres binaires
- Manipuler les parcours classiques
- Étudier les propriétés (complet, parfait, équilibré)
- Servir de base pour des projets plus avancés (BST, AVL, etc.)

--

## 📜 Licence

Projet à but éducatif.
Libre d’utilisation et de modification.

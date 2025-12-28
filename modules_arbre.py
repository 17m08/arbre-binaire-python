class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droite = d

class Arbre:
    def __init__(self, racine=None):
        self.racine = racine

    def est_vide(self):
        return self.racine is None
    
    def hauteur(self):
        def hauteur_noeud(noeud):
            if noeud is None:
                return 0
            else:
                return 1 + max(hauteur_noeud(noeud.gauche), hauteur_noeud(noeud.droite))
        return hauteur_noeud(self.racine)

    def taille(self):
        def taille_noeud(noeud):
            if noeud is None:
                return 0
            else:
                return 1 + taille_noeud(noeud.gauche) + taille_noeud(noeud.droite)
        return taille_noeud(self.racine)
    
    def parcours_prefixe(self):
        def prefixe_noeud(noeud):
            if noeud is None:
                return []
            else:
                return [noeud.valeur] + prefixe_noeud(noeud.gauche) + prefixe_noeud(noeud.droite)
        return prefixe_noeud(self.racine)
    
    def parcours_infixe(self):
        def infixe_noeud(noeud):
            if noeud is None:
                return []
            else:
                return infixe_noeud(noeud.gauche) + [noeud.valeur] + infixe_noeud(noeud.droite)
        return infixe_noeud(self.racine)
    
    def parcours_postfixe(self):
        def postfixe_noeud(noeud):
            if noeud is None:
                return []
            else:
                return postfixe_noeud(noeud.gauche) + postfixe_noeud(noeud.droite) + [noeud.valeur]
        return postfixe_noeud(self.racine)
    
    def est_feuille(self):
        return self.racine is not None and self.racine.gauche is None and self.racine.droite is None
    
    def rechercher(self, valeur):
        def rechercher_noeud(noeud, valeur):
            if noeud is None:
                return False
            if noeud.valeur == valeur:
                return True
            return rechercher_noeud(noeud.gauche, valeur) or rechercher_noeud(noeud.droite, valeur)
        return rechercher_noeud(self.racine, valeur)
    
    def est_binaire(self):
        def est_binaire_noeud(noeud):
            if noeud is None:
                return True
            if (noeud.gauche is not None and noeud.gauche.droite is not None and noeud.gauche.gauche is not None) or\
                (noeud.droite is not None and noeud.droite.droite is not None and noeud.droite.gauche is not None):
                return False
            return est_binaire_noeud(noeud.gauche) and est_binaire_noeud(noeud.droite)
        return est_binaire_noeud(self.racine)
    
    def nb_noeuds(self):
        return self.taille()
    
    def nb_feuilles(self):
        def compter_feuilles(noeud):
            if noeud is None:
                return 0
            if noeud.gauche is None and noeud.droite is None:
                return 1
            return compter_feuilles(noeud.gauche) + compter_feuilles(noeud.droite)
        return compter_feuilles(self.racine)
    
    def inserer_bts(self):
        def inserer_noeud(noeud, valeur):
            if noeud is None:
                return Noeud(valeur)
            if valeur < noeud.valeur:
                noeud.gauche = inserer_noeud(noeud.gauche, valeur)
            else:
                noeud.droite = inserer_noeud(noeud.droite, valeur)
            return noeud
        self.racine = inserer_noeud(self.racine, valeur)

    def parcours_largeur(self):
        if self.racine is None:
            return []
        resultat = []
        file = [self.racine]
        while file:
            noeud = file.pop(0)
            resultat.append(noeud.valeur)
            if noeud.gauche is not None:
                file.append(noeud.gauche)
            if noeud.droite is not None:
                file.append(noeud.droite)
        return resultat
    
    def est_complet(self):
        def compter_noeuds(noeud):
            if noeud is None:
                return 0
            return 1 + compter_noeuds(noeud.gauche) + compter_noeuds(noeud.droite)
        
        def est_complet_noeud(noeud, index, nombre_noeuds):
            if noeud is None:
                return True
            if index >= nombre_noeuds:
                return False
            return (est_complet_noeud(noeud.gauche, 2 * index + 1, nombre_noeuds) and
                    est_complet_noeud(noeud.droite, 2 * index + 2, nombre_noeuds))
        
        nombre_noeuds = compter_noeuds(self.racine)
        return est_complet_noeud(self.racine, 0, nombre_noeuds)
    
    def est_parfait(self):
        def hauteur_noeud(noeud):
            if noeud is None:
                return 0
            return 1 + max(hauteur_noeud(noeud.gauche), hauteur_noeud(noeud.droite))
        
        def est_parfait_noeud(noeud, profondeur, niveau=0):
            if noeud is None:
                return True
            if noeud.gauche is None and noeud.droite is None:
                return profondeur == niveau + 1
            if noeud.gauche is None or noeud.droite is None:
                return False
            return (est_parfait_noeud(noeud.gauche, profondeur, niveau + 1) and
                    est_parfait_noeud(noeud.droite, profondeur, niveau + 1))
        
        profondeur = hauteur_noeud(self.racine)
        return est_parfait_noeud(self.racine, profondeur)
    
    def est_equilibre(self):
        def est_equilibre_noeud(noeud):
            if noeud is None:
                return 0, True
            hauteur_gauche, est_gauche_equilibre = est_equilibre_noeud(noeud.gauche)
            hauteur_droite, est_droite_equilibre = est_equilibre_noeud(noeud.droite)
            hauteur = 1 + max(hauteur_gauche, hauteur_droite)
            est_equilibre = (est_gauche_equilibre and est_droite_equilibre and
                             abs(hauteur_gauche - hauteur_droite) <= 1)
            return hauteur, est_equilibre
        _, est_equilibre = est_equilibre_noeud(self.racine)
        return est_equilibre
    
def dessiner(self):
    def dessiner_noeud(noeud, prefixe="", est_gauche=True):
        if noeud is not None:
            print(prefixe + ("|-- " if est_gauche else "`-- ") + str(noeud.valeur))
            dessiner_noeud(noeud.gauche, prefixe + ("|   " if est_gauche else "    "), True)
            dessiner_noeud(noeud.droite, prefixe + ("|   " if est_gauche else "    "), False)
    dessiner_noeud(self.racine)

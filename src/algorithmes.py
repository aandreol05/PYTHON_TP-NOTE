def obtenir_successeur(graphe, sommet) :
    """retourne la liste des sommets directemment accessible depuis 'sommets'"""
    if not graphe.contient_sommet(sommet) :
        raise ValueError(f"Le sommet : {sommet} n'existe pas dans le graphe")

    # les clefs du dictionnaire voisin sont les successeurs direct 
    voisins = graphe.obtenir_voisin(sommet)
    return list(voisins.keys())

def obtenir_predecesseur(graphe, sommet) :
    """retourne la liste des sommets ayant un arc orienté vers 'sommet'"""
    if not graphe.contient_sommet(sommet) :
            raise ValueError(f"Le sommet : {sommet} n'existe pas dans le graphe")

    predecesseurs = []
    # on parcour tous les autres sommets du graphe pour savoir si il y en a un qui pontent vers notre sommet
    for autre_sommet in graphe.obtenir_sommet() :
         if graphe.contient_arc(autre_sommet, sommet) :
              predecesseurs.append(autre_sommet)

    return predecesseurs

def degre_sortant(graphe, sommet) :
     """retourn le nombre d'arc successeur"""
     return len(obtenir_successeur(graphe, sommet))

def degre_entrant(graphe, sommet) :
     """retourn le nombre d'arc predecesseur"""
     return len(obtenir_predecesseur(graphe, sommet))
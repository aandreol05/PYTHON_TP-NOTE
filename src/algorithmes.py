def obtenir_successeur(graphe, sommet) :
    """retourne la liste des sommets directemment accessible depuis 'sommets'"""
    if not graphe.contient_sommet(sommet) :
        raise ValueError(f"Le sommet : {sommet} n'existe pas dans le graphe")

    # les clefs du dictionnaire voisin sont les successeurs direct 
    voisins = graphe.obtenir_voisin(sommet)
    return list(voisins.keys())

    
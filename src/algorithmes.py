from src.graphe import Graphe

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

def degre_total(graphe, sommet) :
    """retourne la somme degre entrant et sortant"""
    return degre_sortant(graphe, sommet) + degre_entrant(graphe, sommet) 

def shortest_path(graphe, depart, arrivee) :
    """calcul le chemin le plus court entre déépart et arrivée
    retourne un tuple : liste du chemin et cout total"""
    if not graphe.contient_sommet(depart) :
        raise ValueError(f"Le sommet : {depart} n'esxiste pas")
    if not graphe.contient_sommet(arrivee) :
        raise ValueError(f"Le sommet : {arrivee} n'esxiste pas")

    # cas ou le depart et l'arrive sont identique
    if depart == arrivee :
        return ([depart], 0.0)

    # on initialise les distance à l'infinie ce qui facilite les mise à jour des distances si on en a pas encore au début
    distances = {}
    predecesseurs = {}
    for sommet in graphe.obtenir_sommet() :
        distances[sommet] = float("inf")
        predecesseurs[sommet] = None
    distances[depart] = 0.0

    non_visites = list(graphe.obtenir_sommet())

    # boucle principale de Dijkstra
    while len(non_visites) > 0 :
        #trouver le sommet non visite avec la plus petite distance du sommet actuelle
        sommet_actuel = None
        plus_petite_distance = float("inf")
        for s in non_visites :
            if distances[s] < plus_petite_distance :
                plus_petite_distance = distances[s]
                sommet_actuel = s

        # si aucun sommet n'est accessible ou si on est à l'arrive on arrete 
        if sommet_actuel is None or sommet_actuel == arrivee :
            break

        non_visites.remove(sommet_actuel)

        # mise à jour des distances des voisins 
        voisins = graphe.obtenir_voisin(sommet_actuel)
        for voisin, poids in voisins.items() :
            if voisin in non_visites :
                nouvelle_distance = distances[sommet_actuel] + poids
                if nouvelle_distance < distances[voisin] :
                    distances[voisin] = nouvelle_distance
                    predecesseurs[voisin] = sommet_actuel

    # verification si l'arrivee est atteignable 
    if distances[arrivee] == float("inf") : 
        return (None, float("inf"))

    # reconstruction du chemin à l'envers 
    chemin = []
    courant = arrivee 
    while courant is not None :
        chemin.append(courant)
        courant = predecesseurs[courant]
    chemin.reverse()

    return (chemin, distances[arrivee])

def shortest_path_avoiding(graphe, depart, arrivee , interdits) :
    """Calculer le chemin le plus court en évitant les sommets dans interdit"""

    if not graphe.contient_sommet(depart) :
        raise ValueError(f"le sommet : {depart} n'existe pas")
    if not graphe.contient_sommet(arrivee) :
            raise ValueError(f"le sommet : {arrivee} n'existe pas")

    # on verrifie que tous les sommet dans interdir existe 
    for s in interdits :
        if not graphe.contient_sommet(s) :
            raise ValueError(f"Le sommet interdit : {s} n'existe pas")

    # si le départ ou l'arrivee est dans inerdit alors aucun chemin possible
    if depart in interdits or arrivee in interdits :
        return (None, float("inf"))

    if depart == arrivee :
        return ([depart], 0.0)

    # initialisation comme dans shortest_path
    distances = {}
    predecesseurs = {}
    for sommet in graphe.obtenir_sommet() :
        distances[sommet] = float("inf")
        predecesseurs[sommet] = None
    distances[depart] = 0.0

    # on retire les sommets interdit 
    non_visites = []
    for sommet in graphe.obtenir_sommet() :
        if not sommet in interdits :
            non_visites.append(sommet)

    # récupération du même code que dans la def shortest_path
    while len(non_visites) > 0 :
        sommet_actuel = None
        plus_petite_distance = float("inf")
        for s in non_visites :
            if distances[s] < plus_petite_distance :
                plus_petite_distance = distances[s]
                sommet_actuel = s
    
        if sommet_actuel is None or sommet_actuel == arrivee :
            break
    
        non_visites.remove(sommet_actuel)
    
        voisins = graphe.obtenir_voisin(sommet_actuel)
        for voisin, poids in voisins.items() :
            if voisin in non_visites :
                nouvelle_distance = distances[sommet_actuel] + poids
                if nouvelle_distance < distances[voisin] :
                    distances[voisin] = nouvelle_distance
                    predecesseurs[voisin] = sommet_actuel
    
    if distances[arrivee] == float("inf") : 
        return (None, float("inf"))
    
    chemin = []
    courant = arrivee 
    while courant is not None :
        chemin.append(courant)
        courant = predecesseurs[courant]
    chemin.reverse()
    
    return (chemin, distances[arrivee])

def intersections(graphe1, graphe2) :
    """Permet d'avoir un graphe avec les sommets, les arc identiques entre graphe1 et graphe2"""

    resultat = Graphe()

    # ajouter le sommet dans resultat si un sommet est dzns les deux graphes
    for sommet in graphe1.obtenir_sommet() :
        if graphe2.contient_sommet(sommet) :
            resultat.ajouter_sommet(sommet)
    
    # ajouter les arcs strictement identique entre les deux graphes
    for sommet in resultat.obtenir_sommet() :
        voisins_g1 = graphe1.obtenir_voisin(sommet)
        for destination, poids in voisins_g1.items() :
            if graphe2.contient_arc(sommet, destination) :
                if graphe2.obtenir_poids(sommet, destination) == poids :
                    resultat.ajouter_arc(sommet, destination, poids)

    return resultat
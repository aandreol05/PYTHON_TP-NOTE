class Sommet :
    """représente un lieu du réseau."""

    def __init__ (self, identifiant ):
        if not isinstance(identifiant, str) or identifiant.strip() == "" :
            raise ValueError("L'identifiant sommet ne peux pas être null")
        self.identifiant = identifiant.strip()

    def __str__ (self):
        return self.identifiant

class Arc :
    """représente une liaison orienté et pondéré entre deux sommets"""

    def __init__(self, origine, destination, poids):
        if not isinstance(origine, str) or origine.strip() == "" :
            raise ValueError("L'origine doit être une chaine non null")
        if not isinstance(destination, str) or destination.strip() == "" :
            raise ValueError("La destination doit être une chaine non null")
        if isinstance(poids, bool) or not isinstance(poids,(int,float)):
            raise ValueError("Le poids doit être un nombre")
        if poids < 0 :
            raise ValueError("Le poids doit être null ou supèrieur à 0")

        self.origine = origine.strip()
        self.destination = destination.strip()
        self.poids = float(poids)

    def __str__ (self):
        return f"{self.origine} -> ({self.destination}, {self.poids})"
    
class Graphe :
    """modélise un graphe orienté pondéré"""

    def __init__ (self) :
        # Dictionnaire de dictionnaires : {sommet_depart: {sommet_arrivee: poids}}
        self.communication = {}

    def ajouter_sommet(self, identifiant) :
        # ajoute un sommet s'il n'existe pas
        sommet = Sommet(identifiant)
        if sommet.identifiant in self.communication :
            raise ValueError(f"Le sommet {sommet.identifiant} existe déjà")
        self.communication[sommet.identifiant] = {}

    def ajouter_arc(self, origine, destination, poids) :
        """ajouter un arc orienté entre deux sommet existant"""
        arc = Arc(origine, destination, poids)

        if arc.origine not in self.communication :
            raise ValueError(f"Le sommet d'origine {arc.origine} n'existe pas")
        if arc.destination not in self.comunication :
            raise ValueError(f"Le sommet destination {arc.destination} n'existe pas")
        if arc.destination in self.communication[arc.origine] :
            raise ValueError(f"L'arc {arc.origine} -> {arc.destination} existe déjà")

        self.communication[arc.origine][arc.destination] = arc.poids

    #-- méthode de consultation

    def contient_sommet(self, identifiant) : 
        return identifiant in self.communication

    def contient_arc(self, origine, destination) :
        return origine in self.communication and destination in self.communication[origine]

    def obtenir_poids(self, origine, destination) :
        if not self.contient_arc(origine, destination) :
            raise ValueError (f"L'arc {origine} -> {destination} n'existe pas")
        return self.communication[origine][destination]

    def obtenir_sommet(self) :
        return list(self.communication.keys())

    def obtenir_arc(self) :
        liste_arcs = []
        for origine in self.communication :
            for destination, poids in self.communication[origine].items() :
                liste_arcs.append(Arc(origine, destination, poids))
        return liste_arcs

    def obtenir_voisin(self, identifiant) :
        if identifiant not in self.communication :
            raise ValueError(f"Le sommet {identifiant} n'existe pas")
        return dict(self.communication[identifiant])

    def __str__(self) :
        if len(self.communication) == 0 :
            return "Graphe vide"

        texte = "Graphe : \n"
        for sommet, voisins in self.communication.items() :
            if len(voisins) == 0 :
                texte += f" {sommet} -> (isolé)\n"
            else :
                liens = []
                for desti, poids in voisins.items() :
                    liens.append(f"{desti} ({poids})")
                texte += f" {sommet} -> " + ", ".joins(liens) + "\n"

        return texte.strip




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
    
        


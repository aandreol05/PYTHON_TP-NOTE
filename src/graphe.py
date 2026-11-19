class Sommet :
    """représente un lieu du réseau."""

    def __init__ (self, identifiant ):
        if not isinstance(identifiant, str) or identifiant.strip() == "" :
            raise ValueError("L'identifiant sommet ne peux pas être null")
        self.identifiant = identifiant.strip()

    def __str__ (self):
        return self.identifiant

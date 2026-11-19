import unittest
from src.graphe import Graphe


class TestPartieA(unittest.TestCase):

    def setUp(self):
        self.g = Graphe()
        self.g.ajouter_sommet("A")
        self.g.ajouter_sommet("B")
        self.g.ajouter_sommet("H")

    def test_sommets_et_doublons(self):
        self.assertEqual(self.g.obtenir_sommet(), ["A", "B", "H"])
        # Doublon interdit
        with self.assertRaises(ValueError):
            self.g.ajouter_sommet("A")
        # Sommet vide interdit
        with self.assertRaises(ValueError):
            self.g.ajouter_sommet("   ")

    def test_arcs_et_orientation(self):
        self.g.ajouter_arc("A", "B", 4)
        self.assertTrue(self.g.contient_arc("A", "B"))
        self.assertFalse(self.g.contient_arc("B", "A"))
        self.assertEqual(self.g.obtenir_poids("A", "B"), 4.0)

    def test_erreurs_arcs(self):
        self.g.ajouter_arc("A", "B", 4)
        # Doublon d'arc
        with self.assertRaises(ValueError):
            self.g.ajouter_arc("A", "B", 10)
        # Sommet inexistant
        with self.assertRaises(ValueError):
            self.g.ajouter_arc("Z", "B", 3)
        # Poids négatif
        with self.assertRaises(ValueError):
            self.g.ajouter_arc("B", "A", -1)

    def test_consultation_et_affichage(self):
        self.g.ajouter_arc("A", "B", 4)
        self.assertEqual(self.g.obtenir_voisin("A"), {"B": 4.0})
        self.assertEqual(self.g.obtenir_voisin("H"), {})
        self.assertEqual(len(self.g.obtenir_arc()), 1)
        # Vérifie que __str__ renvoie bien une chaîne contenant A et B
        affichage = str(self.g)
        self.assertIn("A -> B (4.0)", affichage)


if __name__ == "__main__":
    unittest.main()
import unittest
from src.graphe import from_files
from src.algorithmes import shortest_path_avoiding, intersections


class TestPartieE(unittest.TestCase):

    def setUp(self):
        self.g1 = from_files("data/reseau.txt")
        self.g2 = from_files("data/reseau_secondaire.txt")

    def test_eviter_sommet_C(self):
        # Sans C, le chemin A -> G passe directement par B -> D -> E -> F -> G
        chemin, cout = shortest_path_avoiding(self.g1, "A", "G", ["C"])
        self.assertEqual(chemin, ["A", "B", "D", "E", "F", "G"])
        self.assertEqual(cout, 15.0)

    def test_eviter_depart_ou_arrivee(self):
        chemin, cout = shortest_path_avoiding(self.g1, "A", "G", ["A"])
        self.assertIsNone(chemin)
        self.assertEqual(cout, float("inf"))

    def test_aucun_chemin_apres_blocage(self):
        # Bloquer D et G coupe tout accès vers G
        chemin, cout = shortest_path_avoiding(self.g1, "A", "G", ["D", "G"])
        self.assertIsNone(chemin)
        self.assertEqual(cout, float("inf"))

    def test_intersection_graphes(self):
        g_inter = intersections(self.g1, self.g2)
        # Sommets communs : A, B, C, D (Z n'est que dans g2 ; E, F, G, H que dans g1)
        self.assertEqual(g_inter.obtenir_sommet(), ["A", "B", "C", "D"])
        # Arcs identiques (même poids) : A->B (4), C->B (1), B->D (5)
        # A->C est exclu car poids 2 dans g1 mais 5 dans g2
        self.assertTrue(g_inter.contient_arc("A", "B"))
        self.assertTrue(g_inter.contient_arc("C", "B"))
        self.assertTrue(g_inter.contient_arc("B", "D"))
        self.assertFalse(g_inter.contient_arc("A", "C"))
        self.assertEqual(len(g_inter.obtenir_arc()), 3)


if __name__ == "__main__":
    unittest.main()
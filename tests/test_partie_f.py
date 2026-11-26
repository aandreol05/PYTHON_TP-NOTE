import unittest
from src.graphe import from_files
from src.algorithmes import has_cycle, topological_sort


class TestPartieF(unittest.TestCase):

    def setUp(self):
        self.g = from_files("data/reseau.txt")

    def test_graphe_acyclique_reseau_initial(self):
        # le réseau de base n'a aucun cycle
        self.assertFalse(has_cycle(self.g))

        ordre = topological_sort(self.g)
        # vérifie que tous les 8 sommets sont présents dans l'ordre
        self.assertEqual(len(ordre), 8)
        # vérifie que pour chaque arc u -> v, u apparaît bien avant v dans l'ordre
        for u in self.g.obtenir_sommet():
            for v in self.g.obtenir_voisin(u):
                self.assertLess(ordre.index(u), ordre.index(v))

    def test_graphe_avec_cycle(self):
        # on ajoute l'arc G -> A pour fermer une boucle A -> ... -> G -> A
        self.g.ajouter_arc("G", "A", 1)

        self.assertTrue(has_cycle(self.g))
        with self.assertRaises(ValueError):
            topological_sort(self.g)

    def test_boucle_sur_soi_meme(self):
        # un arc H -> H est aussi un cycle
        self.g.ajouter_arc("H", "H", 2)

        self.assertTrue(has_cycle(self.g))
        with self.assertRaises(ValueError):
            topological_sort(self.g)


if __name__ == "__main__":
    unittest.main()
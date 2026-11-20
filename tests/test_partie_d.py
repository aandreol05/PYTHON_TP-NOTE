import unittest
from src.graphe import from_files
from src.algorithmes import shortest_path


class TestPartieD(unittest.TestCase):

    def setUp(self):
        self.g = from_files("data/reseau.txt")

    def test_plus_court_chemin_A_vers_G(self):
        chemin, cout = shortest_path(self.g, "A", "G")
        self.assertEqual(chemin, ["A", "C", "B", "D", "E", "F", "G"])
        self.assertEqual(cout, 14.0)

    def test_depart_egal_arrivee(self):
        chemin, cout = shortest_path(self.g, "C", "C")
        self.assertEqual(chemin, ["C"])
        self.assertEqual(cout, 0.0)

    def test_aucun_chemin_vers_sommet_isole(self):
        chemin, cout = shortest_path(self.g, "A", "H")
        self.assertIsNone(chemin)
        self.assertEqual(cout, float("inf"))

    def test_sommet_inexistant(self):
        with self.assertRaises(ValueError):
            shortest_path(self.g, "A", "Z")


if __name__ == "__main__":
    unittest.main()
import unittest
from src.graphe import from_files
from src.algorithmes import (
    obtenir_successeur,
    obtenir_predecesseur,
    degre_entrant,
    degre_sortant,
    degre_total,
)


class TestPartieC(unittest.TestCase):

    def setUp(self):
        self.g = from_files("data/reseau.txt")

    def test_sommet_isole_H(self):
        self.assertEqual(obtenir_predecesseur(self.g, "H"), [])
        self.assertEqual(obtenir_successeur(self.g, "H"), [])
        self.assertEqual(degre_entrant(self.g, "H"), 0)
        self.assertEqual(degre_sortant(self.g, "H"), 0)
        self.assertEqual(degre_total(self.g, "H"), 0)

    def test_sommet_B(self):
        self.assertEqual(obtenir_predecesseur(self.g, "B"), ["A", "C"])
        self.assertEqual(obtenir_successeur(self.g, "B"), ["D", "G"])
        self.assertEqual(degre_entrant(self.g, "B"), 2)
        self.assertEqual(degre_sortant(self.g, "B"), 2)
        self.assertEqual(degre_total(self.g, "B"), 4)

    def test_sommet_D(self):
        self.assertEqual(obtenir_predecesseur(self.g, "D"), ["B", "C"])
        self.assertEqual(obtenir_successeur(self.g, "D"), ["E", "F"])
        self.assertEqual(degre_entrant(self.g, "D"), 2)
        self.assertEqual(degre_sortant(self.g, "D"), 2)
        self.assertEqual(degre_total(self.g, "D"), 4)

    def test_sommet_inexistant(self):
        with self.assertRaises(ValueError):
            degre_total(self.g, "Z")


if __name__ == "__main__":
    unittest.main()
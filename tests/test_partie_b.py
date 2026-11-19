import unittest
import os
from src.graphe import from_files


class TestPartieB(unittest.TestCase):

    def test_fichier_valide(self):
        g = from_files("data/reseau.txt")
        self.assertEqual(g.obtenir_sommet(), ["A", "B", "C", "D", "E", "F", "G", "H"])
        self.assertEqual(len(g.obtenir_arc()), 11)
        self.assertEqual(g.obtenir_voisin("H"), {})

    def test_fichier_inexistant(self):
        with self.assertRaises(FileNotFoundError):
            from_files("data/n_existe_pas.txt")

    def test_ligne_mal_formee(self):
        # On crée un petit fichier avec une erreur (il manque le poids)
        f = open("data/test_erreur.txt", "w", encoding="utf-8")
        f.write("Sommets: A, B\n")
        f.write("A;B\n")
        f.close()

        with self.assertRaises(ValueError):
            from_files("data/test_erreur.txt")

        os.remove("data/test_erreur.txt")

    def test_poids_invalide_et_sommet_inconnu(self):
        # Test 1 : poids négatif
        f = open("data/test_erreur.txt", "w", encoding="utf-8")
        f.write("Sommets: A, B\n")
        f.write("A;B;-4\n")
        f.close()

        with self.assertRaises(ValueError):
            from_files("data/test_erreur.txt")

        # Test 2 : sommet inconnu Z
        f = open("data/test_erreur.txt", "w", encoding="utf-8")
        f.write("Sommets: A, B\n")
        f.write("A;Z;4\n")
        f.close()

        with self.assertRaises(ValueError):
            from_files("data/test_erreur.txt")

        os.remove("data/test_erreur.txt")


if __name__ == "__main__":
    unittest.main()
# Gestionnaire et Analyseur de Réseau Orienté Pondéré

Application Python développée en programmation orientée objet permettant de modéliser, charger, analyser et parcourir un réseau représenté sous forme de **graphe orienté pondéré**.

---

## Architecture du projet

```text
TP-NOTE/
├── data/
│   ├── reseau.txt              # Réseau principal de référence
│   └── reseau_secondaire.txt   # Second réseau utilisé pour les tests d'intersection
├── src/
│   ├── __init__.py
│   ├── graphe.py               # Modélisation (Graphe, Sommet, Arc) et lecture de fichiers (from_files)
│   └── algorithmes.py          # Analyse des degrés, Dijkstra, contraintes, intersection et détection de cycles
├── tests/
│   ├── __init__.py
│   ├── test_partie_a.py        # Tests de modélisation et validation des données
│   ├── test_partie_b.py        # Tests d'importation de fichiers et gestion d'erreurs
│   ├── test_partie_c.py        # Tests des degrés, prédécesseurs et successeurs
│   ├── test_partie_d.py        # Tests du plus court chemin (Dijkstra)
│   ├── test_partie_e.py        # Tests avec sommets interdits et intersection de graphes
│   └── test_partie_f.py        # Tests de détection de cycles et tri topologique (algorithme de Kahn)
├── main.py                     # Interface console interactive
└── README.md
```

---

## Prérequis et exécution

* **Version de Python :** Python 3.10 ou supérieur (aucune bibliothèque externe obligatoire pour le fonctionnement du cœur du programme).
* **Dépendance optionnelle (affichage coloré des tests) :** `green` (`pip3 install green`).

### Lancer l'application interactive
Depuis la racine du projet :
```bash
python3 main.py
```

### Lancer la suite de tests unitaires
Avec la bibliothèque standard `unittest` :
```bash
python3 -m unittest discover -v -s tests
```

Ou avec l'interface colorée `green` :
```bash
green -vv tests
```

---

## Format des fichiers de données

Les fichiers réseau placés dans `data/` respectent la structure suivante :
```text
Sommets: A, B, C, D, E, F, G, H
A;B;4
A;C;2
C;B;1
```
* **Première ligne :** liste des sommets déclarée après le préfixe `Sommets:`.
* **Lignes suivantes :** arcs orientés au format `origine;destination;poids` (avec un poids numérique positif ou nul).
* **Gestion des erreurs :** toute anomalie dans le fichier (fichier introuvable, en-tête invalide, ligne mal formée, sommet inconnu ou poids négatif) entraîne le rejet complet du chargement afin de garantir l'intégrité du graphe en mémoire.

---

## Fonctionnalités implémentées

1. **Modélisation orientée objet (`src/graphe.py`) :**
   * Classes `Sommet`, `Arc` et `Graphe` reposant sur une structure de dictionnaire de dictionnaires pour un accès rapide et une prévention native des doublons.
   * Validation stricte des identifiants (non vides) et des poids ($\ge 0$).
2. **Chargement depuis un fichier (`from_files`) :**
   * Construction automatique d'une instance `Graphe` à partir d'un fichier texte.
3. **Analyse structurelle (`src/algorithmes.py`) :**
   * Récupération des successeurs (`obtenir_successeur`) et prédécesseurs (`obtenir_predecesseur`).
   * Calcul des degrés entrant (`degre_entrant`), sortant (`degre_sortant`) et total (`degre_total`), y compris sur les sommets isolés.
4. **Recherche d'itinéraires :**
   * `shortest_path` : calcul du chemin de coût minimal entre deux sommets via l'algorithme de **Dijkstra**.
   * `shortest_path_avoiding` : recherche du plus court chemin tout en contournant une liste de sommets interdits.
5. **Comparaison et ordonnancement :**
   * `intersection` : génération d'un nouveau graphe contenant uniquement les sommets communs et les arcs strictement identiques (même origine, destination et poids) entre deux réseaux.
   * `has_cycle` et `topological_sort` : détection de circuits et calcul d'un ordre topologique via l'**algorithme de Kahn**.

---

## Démarche, accompagnement et ressources utilisées

Pour mener à bien ce projet, j'ai combiné des recherches documentaires sur des sites de référence en programmation avec un accompagnement ponctuel via un assistant IA (Gemini) :

### Apport de l'assistant IA
* **Compréhension de la théorie des graphes :** N'ayant pas encore abordé la théorie des graphes en cours avant ce TP, l'assistant m'a aidé à assimiler les notions fondamentales (graphes orientés et pondérés, degrés entrants/sortants, principe de relâchement des distances dans l'algorithme de Dijkstra et fonctionnement de l'algorithme de Kahn pour la détection de cycles et le tri topologique).
* **Syntaxes et subtilités Python :** J'ai eu recours à une aide ponctuelle sur certaines syntaxes spécifiques du langage, comme la distinction entre booléens et entiers lors de la validation des types (`isinstance(poids, bool)`), la gestion sécurisée de l'ouverture de fichiers (`with open(...)`), l'utilisation de l'infini (`float("inf")`) ou encore les méthodes de classe (`@classmethod`).
* **Réalisation des tests unitaires :** L'assistant m'a guidé pour structurer mes fichiers de tests avec le module `unittest` (`setUp`, `assertRaises`, vérification des cas limites et exécution automatique de l'ensemble des tests).

### Sites web et documentations de référence
* **[Documentation officielle Python (docs.python.org)](https://docs.python.org/fr/3/)** : référence principale pour la manipulation des dictionnaires, la levée et la capture d'exceptions (`ValueError`, `FileNotFoundError`), la lecture de fichiers et l'utilisation de `unittest`.
* **[Real Python (realpython.com)](https://realpython.com/)** : tutoriels sur l'organisation d'un projet Python en modules (`src/`, `tests/`), les bonnes pratiques de programmation orientée objet et l'écriture de tests unitaires propres.
* **[GeeksforGeeks (geeksforgeeks.org)](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)** : fiches explicatives et schémas sur les structures de données pour les graphes, le déroulement pas à pas de l'algorithme de Dijkstra et le tri topologique de Kahn.
* **[VisuAlgo (visualgo.net)](https://visualgo.net/en/sssp)** : outil de visualisation interactive utilisé pour observer étape par étape le parcours des sommets et la mise à jour des distances dans un graphe orienté.
* **[Stack Overflow (stackoverflow.com)](https://stackoverflow.com/)** : recherche de solutions sur la gestion des imports entre dossiers (`__init__.py`) et la résolution d'avertissements liés aux ressources fichiers (`ResourceWarning`).
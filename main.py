from src.graphe import Graphe, from_files
from src.algorithmes import (
    obtenir_successeur,
    obtenir_predecesseur,
    degre_entrant,
    degre_sortant,
    degre_total,
    shortest_path,
    shortest_path_avoiding,
    intersections,
    has_cycle,
    topological_sort,
)


def afficher_menu():
    print("\n" + "=" * 50)
    print("         GESTIONNAIRE DE RÉSEAU ORIENTÉ")
    print("=" * 50)
    print("1.  Charger un graphe depuis un fichier")
    print("2.  Afficher le graphe actuel")
    print("3.  Ajouter un sommet")
    print("4.  Ajouter un arc")
    print("5.  Analyser un sommet (degrés, voisins)")
    print("6.  Calculer le plus court chemin (Dijkstra)")
    print("7.  Plus court chemin avec sommets interdits")
    print("8.  Calculer l'intersection avec un autre fichier")
    print("9.  Vérifier la présence d'un cycle (Bonus)")
    print("10. Calculer l'ordre topologique (Bonus)")
    print("0.  Quitter")
    print("=" * 50)


def main():
    # Chargement automatique du réseau par défaut au démarrage
    try:
        graphe = from_files("data/reseau.txt")
        print("Réseau par défaut 'data/reseau.txt' chargé.")
    except Exception:
        graphe = Graphe()
        print("Aucun fichier par défaut trouvé. Départ avec un graphe vide.")

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        try:
            if choix == "1":
                chemin = input("Chemin du fichier (ex: data/reseau.txt) : ").strip()
                graphe = from_files(chemin)
                print(f"Graphe chargé avec succès ({len(graphe.obtenir_sommet())} sommets).")

            elif choix == "2":
                print("\n--- État du graphe ---")
                print(graphe)

            elif choix == "3":
                sommet = input("Nom du nouveau sommet : ").strip()
                graphe.ajouter_sommet(sommet)
                print(f"Sommet '{sommet}' ajouté.")

            elif choix == "4":
                origine = input("Sommet d'origine : ").strip()
                destination = input("Sommet de destination : ").strip()
                poids = float(input("Poids de l'arc : ").strip())
                graphe.ajouter_arc(origine, destination, poids)
                print(f"Arc {origine} -> {destination} ({poids}) ajouté.")

            elif choix == "5":
                sommet = input("Nom du sommet à analyser : ").strip()
                print(f"\nAnalyse du sommet '{sommet}' :")
                print(f"  - Prédécesseurs : {obtenir_predecesseur(graphe, sommet)}")
                print(f"  - Successeurs   : {obtenir_successeur(graphe, sommet)}")
                print(f"  - Degré entrant : {degre_entrant(graphe, sommet)}")
                print(f"  - Degré sortant : {degre_sortant(graphe, sommet)}")
                print(f"  - Degré total   : {degre_total(graphe, sommet)}")

            elif choix == "6":
                depart = input("Sommet de départ : ").strip()
                arrivee = input("Sommet d'arrivée : ").strip()
                chemin, cout = shortest_path(graphe, depart, arrivee)
                if chemin is None:
                    print(f"Aucun chemin possible entre '{depart}' et '{arrivee}'.")
                else:
                    trajet = " -> ".join(chemin)
                    print(f"Plus court chemin : {trajet} (coût total : {cout})")

            elif choix == "7":
                depart = input("Sommet de départ : ").strip()
                arrivee = input("Sommet d'arrivée : ").strip()
                texte_interdits = input("Sommets à éviter séparés par des virgules (ex: C, D) : ").strip()

                interdits = []
                if texte_interdits != "":
                    for s in texte_interdits.split(","):
                        interdits.append(s.strip())

                chemin, cout = shortest_path_avoiding(graphe, depart, arrivee, interdits)
                if chemin is None:
                    print(f"Aucun chemin possible entre '{depart}' et '{arrivee}' en évitant {interdits}.")
                else:
                    trajet = " -> ".join(chemin)
                    print(f"Chemin trouvé : {trajet} (coût total : {cout})")

            elif choix == "8":
                chemin2 = input("Chemin du second fichier (ex: data/reseau_secondaire.txt) : ").strip()
                graphe2 = from_files(chemin2)
                g_inter = intersections(graphe, graphe2)
                print("\n--- Graphe intersection ---")
                print(g_inter)

            elif choix == "9":
                if has_cycle(graphe):
                    print("Résultat : Le graphe contient au moins un cycle.")
                else:
                    print("Résultat : Le graphe est acyclique (aucun cycle détecté).")

            elif choix == "10":
                ordre = topological_sort(graphe)
                print("Ordre topologique :", " -> ".join(ordre))

            elif choix == "0":
                print("Fermeture du programme.")
                break

            else:
                print("Choix invalide, veuillez saisir un chiffre entre 0 et 10.")

        except (ValueError, FileNotFoundError) as erreur:
            print(f"\n[Erreur] {erreur}")


if __name__ == "__main__":
    main()
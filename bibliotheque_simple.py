# Partie 1 : Gestion d'une bibliothèque sans POO

livres = []


def menu():
    print("\n=== Bibliothèque ===")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")
    return input("Votre choix : ")


def main():
    while True:
        choix = menu()
        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            afficher_livres()
        elif choix == "3":
            rechercher_livre()
        elif choix == "4":
            supprimer_livre()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()

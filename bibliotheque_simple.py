# Partie 1 : Gestion d'une bibliothèque sans POO

livres = []
prochain_id = 1


def ajouter_livre():
    global prochain_id
    titre = input("Titre du livre : ").strip()
    auteur = input("Auteur : ").strip()
    livre = {
        "id": prochain_id,
        "titre": titre,
        "auteur": auteur,
        "disponible": True,
    }
    livres.append(livre)
    prochain_id += 1
    print(f"Livre '{titre}' ajouté avec succès (ID: {livre['id']}).")


def afficher_livres():
    if not livres:
        print("Aucun livre dans la bibliothèque.")
        return
    print(f"\n{'ID':<5} {'Titre':<30} {'Auteur':<25} {'Disponible'}")
    print("-" * 65)
    for livre in livres:
        dispo = "Oui" if livre["disponible"] else "Non"
        print(f"{livre['id']:<5} {livre['titre']:<30} {livre['auteur']:<25} {dispo}")


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

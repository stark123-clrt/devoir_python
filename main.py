# Point d'entrée principal — Partie 2 (POO)

from models import Bibliotheque, Utilisateur, Livre, LivreAudio, BandeDessinee, Ebook

bibliotheque = Bibliotheque("Bibliothèque Centrale")
utilisateurs = {}
utilisateur_actif = None


# ── Helpers ──────────────────────────────────────────────────────────────────

def choisir_utilisateur():
    global utilisateur_actif
    if not utilisateurs:
        print("Aucun utilisateur enregistré. Créez-en un d'abord.")
        return
    print("\nUtilisateurs disponibles :")
    for nom in utilisateurs:
        print(f"  - {nom}")
    nom = input("Nom de l'utilisateur : ").strip()
    if nom in utilisateurs:
        utilisateur_actif = utilisateurs[nom]
        print(f"Utilisateur actif : {utilisateur_actif.nom}")
    else:
        print("Utilisateur introuvable.")


def creer_utilisateur():
    nom = input("Nom du nouvel utilisateur : ").strip()
    if not nom:
        print("Nom invalide.")
        return
    if nom in utilisateurs:
        print("Cet utilisateur existe déjà.")
        return
    utilisateurs[nom] = Utilisateur(nom)
    print(f"Utilisateur '{nom}' créé.")


# ── Menu livres ───────────────────────────────────────────────────────────────

def menu_ajouter_livre():
    print("\nType de livre :")
    print("  1. Livre classique")
    print("  2. Livre audio")
    print("  3. Bande dessinée")
    print("  4. Ebook")
    choix = input("Votre choix : ").strip()

    titre = input("Titre : ").strip()
    auteur = input("Auteur : ").strip()

    if choix == "1":
        livre = Livre(titre, auteur)
    elif choix == "2":
        try:
            duree = int(input("Durée (minutes) : "))
        except ValueError:
            print("Durée invalide.")
            return
        livre = LivreAudio(titre, auteur, duree)
    elif choix == "3":
        illustrateur = input("Illustrateur : ").strip()
        livre = BandeDessinee(titre, auteur, illustrateur)
    elif choix == "4":
        fmt = input("Format (pdf/epub/mobi) : ").strip()
        livre = Ebook(titre, auteur, fmt)
    else:
        print("Choix invalide.")
        return

    bibliotheque.ajouter_livre(livre)


def menu_supprimer_livre():
    bibliotheque.afficher_livres()
    if not bibliotheque.livres:
        return
    try:
        id_cible = int(input("ID du livre à supprimer : "))
    except ValueError:
        print("ID invalide.")
        return
    bibliotheque.supprimer_livre(id_cible)


def menu_rechercher_livre():
    terme = input("Rechercher (titre ou auteur) : ").strip()
    resultats = bibliotheque.rechercher_livre(terme)
    if not resultats:
        print("Aucun résultat.")
    else:
        print(f"{len(resultats)} résultat(s) :")
        for livre in resultats:
            print(f"  {livre}")


# ── Menu emprunts ─────────────────────────────────────────────────────────────

def menu_emprunter():
    if not utilisateur_actif:
        print("Aucun utilisateur actif. Sélectionnez-en un d'abord.")
        return
    bibliotheque.afficher_livres()
    try:
        id_cible = int(input("ID du livre à emprunter : "))
    except ValueError:
        print("ID invalide.")
        return
    for livre in bibliotheque.livres:
        if livre.id == id_cible:
            utilisateur_actif.emprunter_livre(livre)
            return
    print("Livre introuvable.")


def menu_retourner():
    if not utilisateur_actif:
        print("Aucun utilisateur actif. Sélectionnez-en un d'abord.")
        return
    utilisateur_actif.afficher_emprunts()
    if not utilisateur_actif.livres_empruntes:
        return
    try:
        id_cible = int(input("ID du livre à retourner : "))
    except ValueError:
        print("ID invalide.")
        return
    for livre in utilisateur_actif.livres_empruntes:
        if livre.id == id_cible:
            utilisateur_actif.retourner_livre(livre)
            return
    print("Livre introuvable dans vos emprunts.")


# ── Menu principal ────────────────────────────────────────────────────────────

def menu():
    actif = utilisateur_actif.nom if utilisateur_actif else "aucun"
    print(f"\n=== {bibliotheque.nom} === (utilisateur: {actif})")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Créer un utilisateur")
    print("6. Changer d'utilisateur actif")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Voir mes emprunts")
    print("0. Quitter")
    return input("Votre choix : ").strip()


def main():
    # Données de démonstration
    bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry"))
    bibliotheque.ajouter_livre(LivreAudio("Sapiens", "Yuval Noah Harari", 915))
    bibliotheque.ajouter_livre(BandeDessinee("Astérix le Gaulois", "Goscinny", "Uderzo"))
    bibliotheque.ajouter_livre(Ebook("Clean Code", "Robert C. Martin", "pdf"))

    while True:
        choix = menu()
        if choix == "1":
            menu_ajouter_livre()
        elif choix == "2":
            bibliotheque.afficher_livres()
        elif choix == "3":
            menu_rechercher_livre()
        elif choix == "4":
            menu_supprimer_livre()
        elif choix == "5":
            creer_utilisateur()
        elif choix == "6":
            choisir_utilisateur()
        elif choix == "7":
            menu_emprunter()
        elif choix == "8":
            menu_retourner()
        elif choix == "9":
            if utilisateur_actif:
                utilisateur_actif.afficher_emprunts()
            else:
                print("Aucun utilisateur actif.")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()

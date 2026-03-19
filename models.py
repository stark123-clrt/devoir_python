# Partie 2 : Modèles orientés objet

_compteur_id = 0


def _nouveau_id():
    global _compteur_id
    _compteur_id += 1
    return _compteur_id


class Livre:
    """Livre de base."""

    def __init__(self, titre, auteur):
        self.id = _nouveau_id()
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if not self.disponible:
            print(f"'{self.titre}' est déjà emprunté.")
            return False
        self.disponible = False
        print(f"'{self.titre}' emprunté avec succès.")
        return True

    def retourner(self):
        if self.disponible:
            print(f"'{self.titre}' n'était pas emprunté.")
            return False
        self.disponible = True
        print(f"'{self.titre}' retourné avec succès.")
        return True

    def type_livre(self):
        return "Livre classique"

    def __str__(self):
        dispo = "Disponible" if self.disponible else "Emprunté"
        return f"[{self.id}] {self.titre} — {self.auteur} ({self.type_livre()}) [{dispo}]"


class LivreAudio(Livre):
    """Livre disponible en format audio."""

    def __init__(self, titre, auteur, duree_minutes):
        super().__init__(titre, auteur)
        self.duree_minutes = duree_minutes

    def type_livre(self):
        return f"Livre audio ({self.duree_minutes} min)"


class BandeDessinee(Livre):
    """Bande dessinée avec un illustrateur."""

    def __init__(self, titre, auteur, illustrateur):
        super().__init__(titre, auteur)
        self.illustrateur = illustrateur

    def type_livre(self):
        return f"Bande dessinée (ill. {self.illustrateur})"


class Ebook(Livre):
    """Livre numérique avec format de fichier."""

    def __init__(self, titre, auteur, format_fichier):
        super().__init__(titre, auteur)
        self.format_fichier = format_fichier.upper()

    def type_livre(self):
        return f"Ebook ({self.format_fichier})"


class Utilisateur:
    """Représente un membre de la bibliothèque."""

    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            if livre.retourner():
                self.livres_empruntes.remove(livre)
        else:
            print(f"{self.nom} n'a pas emprunté '{livre.titre}'.")

    def afficher_emprunts(self):
        if not self.livres_empruntes:
            print(f"{self.nom} n'a aucun emprunt en cours.")
        else:
            print(f"Emprunts de {self.nom} :")
            for livre in self.livres_empruntes:
                print(f"  - {livre}")

    def __str__(self):
        nb = len(self.livres_empruntes)
        return f"Utilisateur: {self.nom} ({nb} emprunt(s))"


class Bibliotheque:
    """Gère la collection de livres."""

    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté à la bibliothèque.")

    def supprimer_livre(self, id_livre):
        for i, livre in enumerate(self.livres):
            if livre.id == id_livre:
                self.livres.pop(i)
                print(f"Livre ID {id_livre} supprimé.")
                return
        print("Livre introuvable.")

    def rechercher_livre(self, terme):
        terme = terme.lower()
        resultats = [
            l for l in self.livres
            if terme in l.titre.lower() or terme in l.auteur.lower()
        ]
        return resultats

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
            return
        print(f"\n=== {self.nom} — {len(self.livres)} livre(s) ===")
        for livre in self.livres:
            print(f"  {livre}")

    def __str__(self):
        return f"Bibliothèque '{self.nom}' ({len(self.livres)} livres)"

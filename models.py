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

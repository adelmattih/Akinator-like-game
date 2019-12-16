

# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:29:30 2019

@author: paul
Ce code réalise un tout petit Akinator à partir de la base de donné qui correspond au fichier text 8personnages,
après essai sur les 8 personnages le programme arrive bien a devinner à qui on pense.
Il faudra par la suite pouvoir exécuter ce code sur une base de donnée plus importante.

"""

from math import log

class Feuille:
   """
       Une feuille contient uniquement une valeur:
           - l'étiquette (str)
   """

   def __init__(self, etiquette):
       """
           etiquette doit obligatoirement être un str
       """
       if not isinstance(etiquette, str):
           raise TypeError("etiquette doit être un str et pas un {}" \
                           .format(type(etiquette)))
       self.etiquette = etiquette

class Noeud:
   """
       Un noeud a deux valeurs :
           - un dictionnaire d'enfants (dict)
           - l'attribut testé (str)
   """

   def __init__(self, attribut):
       """
           attribut_teste est le nom de l'attribut stocké dans un str
       """
       if not isinstance(attribut, str):
           raise TypeError("attribute_teste doit être un str et pas un {}" \
                           .format(type(attribut)))
       #initialisation des valeurs de l'objet
       self.enfants = dict()
       self.attribut_teste = attribut

class Exemple:
   """
       Un exemple contient 2 valeurs :
           - un dictionnaire d'attributs (dict)
           - une étiquette (str)
   """

   def __init__(self, noms_attributs, valeurs_attributs, etiquette=""):
       """
           etiquette peut être non précisée en quel cas on aurait
           un exemple non étiqueté
       """
       #si on a un problème de types
       if not isinstance(noms_attributs, list) \
       or not isinstance(valeurs_attributs, list):
           raise TypeError("noms_attributs et valeurs_attributs doivent être" \
                           " des listes et pas des {0} et {1}" \
                           .format(type(noms_attributs),
                                   type(valeurs_attributs)))
       if not isinstance(etiquette, str):
           raise TypeError("etiquette doit être un str et pas un {}" \
                           .format(type(etiquette)))
       #si les deux listes n'ont pas le même nombre d'éléments
       if len(valeurs_attributs) != len(noms_attributs):
           raise ValueError("noms_attributs et valeurs_attributs doivent " \
                            "avoir le même nombre d'éléments")
       self.etiquette = etiquette
       self.dict_attributs = dict()
       #on ajoute chaque attribut au dictionnaire
       for i in range(len(noms_attributs)):
           self.dict_attributs[noms_attributs[i]] = valeurs_attributs[i]

class Ensemble:
   """
       Un ensemble contient deux valeurs :
           - les noms des attributs (list)
           - les exemples (list)
   """

   def __init__(self, chemin=""):
       """
           chemin est l'emplacement du fichier contenant les données.
           Cette variable peut être non précisée en quel cas les variables
               seront initialisées comme des listes vides.
       """
       #Python est un langage à typage dynamique fort,
       #il faut donc vérifier que l'utilisateur ne fait pas n'importe quoi
       #en passant autre chose qu'un str
       if not isinstance(chemin, str):
           raise TypeError("chemin doit être un str et non {}" \
                           .format(type(chemin)))
       if chemin == "":
           #initialisation en listes vides
           self.liste_attributs = list()
           self.liste_exemples = list()
       else:
           with open(chemin, 'r') as fichier:
               #on stocke chaque mot de la première ligne dans liste_attributs
               self.liste_attributs = \
                               fichier.readline().lower().strip().split(' ')
               #ensuite on stocke la liste d'exemples dans liste_exemples
               self.liste_exemples = self.liste_en_exemples(
                                       fichier.read().strip().lower().split('\n'),
                                       self.liste_attributs
                                     )

   def __len__(self):
       """
           retourne la longueur de l'ensemble
       """
       return len(self.liste_exemples)

   @staticmethod
   def liste_en_exemples(exemples, noms_attributs):
       """
           retourne une liste d'exemples sur base d'une liste de str contenant
           les valeurs et d'une liste de str contenant les noms des attributs
       """
       #on initialise la liste à retourner
       ret = list()
       for ligne in exemples:
           #on stocke chaque mot de la ligne dans une liste attributs
           attributs = ligne.lower().strip().split(' ')
           #met l'étiquette par défaut si elle n'est pas dans la ligne
           etiquette = attributs[-1] if len(attributs) != len(noms_attributs) \
                                     else ""
           #on ajoute un objet de type Exemple contenant la ligne
           ret.append(Exemple(noms_attributs,
                              attributs[:len(noms_attributs)],
                              etiquette))
       return ret

   def etiquettes_possibles(self):
       """
           retourne une liste contenant les étiquettes de l'ensemble
       """
       #on initialise la valeur de retour
       ret = list()
       #pour chaque exemple de l'ensemble
       for exemple in self.liste_exemples:
           #si l'étiquette n'est pas déjà dans la liste
           if not exemple.etiquette in ret:
               #on l'ajoute
               ret.append(exemple.etiquette)
       return ret

   def sous_ensemble_etiquette(self, etiquette):
       """
           retourne un ensemble contenant uniquement les exemples ayant
           etiquette comme étiquette
       """
       #initialisation de la valeur de retour
       ret = Ensemble()
       #on copie la liste d'attributs
       ret.liste_attributs = self.liste_attributs[:]
       #pour chaque exemple de l'ensemble initial
       for exemple in self.liste_exemples:
           #si l'étiquette est bonne
           if exemple.etiquette == etiquette:
               #on l'ajoute au sous-ensemble
               ret.liste_exemples.append(exemple)
       return ret

   def sous_ensemble_attribut(self, nom_attribut, valeur):
       """
           retourne un sous-ensemble contenant uniquement les exemples ayant
           la bonne valeur pour l'attribut
       """
       ret = Ensemble()
       #on prend tous les attributs sauf celui passé en paramètre
       ret.liste_attributs = self.liste_attributs[:]
       ret.liste_attributs.remove(nom_attribut)
       #pour chaque exemple de l'ensemble
       for exemple in self.liste_exemples:
           #s'il a la bonne valeur
           if exemple.dict_attributs[nom_attribut] == valeur:
               #on l'ajoute
               ret.liste_exemples.append(exemple)
       #et on retourne la liste
       return ret

   def entropie(self):
       """
           retourne l'entropie de Shannon de l'ensemble
       """
       #initialisation de la variable retournée
       ret = 0
       #pour chaque étiquette de l'ensemble
       for etiquette in self.etiquettes_possibles():
           #on crée un sous-ensemble qui ne contient que les éléments de
           #self ayant etiquette comme étiquette
           sous_ensemble = self.sous_ensemble_etiquette(etiquette)
           #on ajoute |c| * log_2(|c|) à ret
           longueur_sous_ensemble = len(sous_ensemble)
           ret += longueur_sous_ensemble * log(longueur_sous_ensemble, 2)
       #on retourne log_2(|S|) - ret/|S|
       return log(len(self), 2) - ret/len(self)

   def attribut_optimal(self):
       """
           retourne un str avec le nom de l'attribut à tester
       """
       max, ret = float("-inf"), ""
       #pour chaque attribut
       for attribut in self.liste_attributs:
           gain = self.gain_entropie(attribut)
           #si le gain d'entropie est le plus grand
           if gain >= max:
               #on le garde en mémoire
               max, ret = gain, attribut
       #et on le retourne
       return ret

   def valeurs_possibles_attribut(self, nom_attribut):
       """
           retourne une liste contenant toutes les
           valeurs possibles de l'attribut
       """
       ret = list()
       #pour chaque exemple
       for exemple in self.liste_exemples:
           #si cette valeur n'est pas encore dans la liste
           if not exemple.dict_attributs[nom_attribut] in ret:
               #on l'ajoute
               ret.append(exemple.dict_attributs[nom_attribut])
       #et on retourne la liste
       return ret

   def gain_entropie(self, nom_attribut):
       """
           retourne la perte d'entropie selon la définition de Ross Quinlan
       """
       somme = 0
       #pour chaque valeur de l'attribut en question
       for valeur in self.valeurs_possibles_attribut(nom_attribut):
           #déclaration de Sv
           sous_ensemble = self.sous_ensemble_attribut(nom_attribut, valeur)
           #somme = somme sur v de |Sv| * Entropie(Sv)
           somme += len(sous_ensemble) * sous_ensemble.entropie()
       #Gain(S, A) = Entropie(S) - 1/|S| * somme
       return self.entropie() - somme/len(self)

T=[]
L=[]
class Arbre_ID3:
   """
       Un arbre ID3 contient deux valeurs :
           - un ensemble d'exemples (Ensemble)
           - un arbre (Noeud)
   """

   def __init__(self, chemin=""):
       """
           chemin est l'emplacement du fichier contenant les données
       """
       #initialisation de l'ensemble avec le fichier dans chemin
       self.ensemble = Ensemble(chemin)
       #initialisation du noeud principal de l'arbre
       self.arbre = None

   def construire(self):
       """
           génère l'arbre sur base de l'ensemble pré-chargé
       """
       self.arbre = self.__construire_arbre(self.ensemble)

   def __construire_arbre(self, ensemble):
       """
           fonction privée et récursive pour la génération de l'arbre
       """
       if not isinstance(ensemble, Ensemble):
           raise TypeError("ensemble doit être un Ensemble et non un {}" \
                           .format(type(ensemble)))
       #si la liste est vide
       if len(ensemble) == 0:
           raise ValueError("la liste d'exemples ne peut être vide !")
       #testons si tous les exemples ont la même étiquette
       if ensemble.entropie() == 0:
           #on retourne l'étiquette en question
           return Feuille(ensemble.liste_exemples[0].etiquette)
       #s'il ne reste d'attribut à tester
       if len(ensemble.liste_attributs) == 0:
           max, etiquette_finale = 0, ""
           #on teste toutes les étiquettes possibles de l'ensemble
           for etiquette in ensemble.etiquettes_possibles():
               sous_ensemble = ensemble.sous_ensemble_etiquette(etiquette)
               #si c'est la plus fréquente, c'est celle qu'on choisit
               if len(sous_ensemble) > max:
                   max, etiquette_finale = len(sous_ensemble), etiquette
           #et on la retourne dans une feuille
           return Feuille(etiquette_finale)

       a_tester = ensemble.attribut_optimal()
       #si on arrive ici, on retourne d'office un nœud et pas une feuille
       noeud = Noeud(a_tester)
       #pour chaque valeur que peut prendre l'attribut à tester
       for valeur in ensemble.valeurs_possibles_attribut(a_tester):
           #on crée un sous-ensemble
           sous_ensemble = ensemble.sous_ensemble_attribut(a_tester, valeur)
           #et on en crée un nouveau nœud
           noeud.enfants[valeur] = self.__construire_arbre(sous_ensemble)
       #on retourne le nœud que l'on vient de créer
       return noeud

   def afficher(self):
       """
           affiche l'entièreté de l'arbre à l'écran
       """
       self.__afficher_arbre(self.arbre)

   def __afficher_arbre(self, noeud, nb_tabs=0):
       """
           selon la convention :
               <texte> <-> nom de l'attribut
               -<texte> <-> valeur de l'attribut
               .<texte> <-> feuille
       """
       #si on a affaire à un nœud
       if isinstance(noeud, Noeud):
           #on affiche le nom de l'attribut testé
           print("Votre personnage est-il " + noeud.attribut_teste + "?")
           rep=input()
           #on parcourt ses enfants
           for enfant in noeud.enfants:
               if rep==str(enfant):
               #on affiche la valeur de l'attribut
                   self.__afficher_arbre(noeud.enfants[enfant], nb_tabs+1)
       #si c'est une feuille
       elif isinstance(noeud, Feuille):
           #on affiche l'étiquette
           print('Vous pensez à :')
           print(noeud.etiquette)
       else:
           raise TypeError("noeud doit être un Noeud/Feuille et pas un {}" \
                           .format(type(noeud)))

   def etiqueter(self, exemple):
       """
           assigne la bonne étiquette à l'exemple passé en paramètre
       """
       #on initialise le nœud actuel avec le haut de l'arbre
       noeud_actuel = self.arbre
       #tant que l'on est sur un nœud et pas sur une feuille,
       #on continue d'explorer
       while not isinstance(noeud_actuel, Feuille):
           #pour savoir quel est le prochain nœud, on récupère d'abord
           #l'attribut testé avec noeud_actuel.attribut_teste puis on récupère
           #la valeur de l'exemple pour cet attribut avec
           #exemple.dict_attributs[noeud_actuel.attribut_teste]
           #puis on prend l'enfant de noeud_actuel ayant cette valeur.
           valeur = exemple.dict_attributs[noeud_actuel.attribut_teste]
           noeud_actuel = noeud_actuel.enfants[valeur]
       #on finit en donnant comme étiquette l'étiquette
       #contenue dans la feuille finale
       exemple.etiquette = noeud_actuel.etiquette

def exemple_utilisation():
   #exemple d'utilisation
   arbre = Arbre_ID3('8_personnages.txt')
   arbre.construire()
   arbre.afficher()



if __name__ == "__main__":
   exemple_utilisation()
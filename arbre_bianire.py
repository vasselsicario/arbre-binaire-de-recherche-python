from __future__ import annotations


class arbre_bianire:
    def __init__(self,int : int) :
        self.int= int
        self.enfant_gauche=None
        self.enfant_droit=None
        
    def getValeurNoeud(self)->int:
        return self.int
    
    def getEnfantGauche(self):
        return self.enfant_gauche
    
    def getEnfantDroit(self):
        return self.enfant_droit
    
    def inserer_noeud(self,valeur : int):
        #si la valeur à inserer < valeur du noeud observé
        if valeur < self.int:
            # si le noeud observé n'a pas d'enfant gauche 
            if self.enfant_gauche == None:
                #on crée un noeud enfant gauche du noeud oberservé
                self.enfant_gauche = arbre_bianire(valeur)
            # le noeud observé à un enfant gauche
            else:
                # on refait la fonction inserer, sur le nouveau noeud qui est l'enfant gauche du précedent noeud observé 
                # on avance donc sur les noeuds jusqu'a ce qu'une place correspondante à la valeur
                self.enfant_gauche.inserer_noeud(valeur)
        #si la valeur à inserer < valeur du noeud observé
        #elif valeur > self.int:
        else:
            #si le noeud observé n'a pas d'enfant droit
            if self.enfant_droit == None:
                #on creer un nouveau noeud sur l'enfant droit du noeud observé
                self.enfant_droit = arbre_bianire(valeur)
            # le noeud observé à un enfant gauche
            else:
                # on refait la fonction inserer, sur le nouveau noeud qui est l'enfant droit du précedent noeud observé 
                # on avance donc sur les noeuds jusqu'a ce qu'une place correspondante à la valeur 
                self.enfant_droit.inserer_noeud(valeur)
                
        
                
    def afficher(self, niv_arbre=0):
        if self.enfant_droit:
            self.enfant_droit.afficher(niv_arbre + 1)
        print(f"{' ' * 4 * niv_arbre}{self.int}")
        if self.enfant_gauche:
            self.enfant_gauche.afficher(niv_arbre + 1)

            
def rechercher(arbre : arbre_bianire,valeur :int):
    if arbre==None:
        return False
    if arbre.int==valeur:
        return True
    elif valeur< arbre.int:
        return rechercher(arbre.enfant_gauche,valeur)
    else:
        return rechercher(arbre.enfant_droit,valeur)
    
    
    
def parcours(arbre : arbre_bianire):
    if arbre == None:
        return ""
    texte =""
    texte =texte +parcours(arbre.enfant_gauche)
    texte = texte+','+ str(arbre.int)
    texte = texte + parcours(arbre.enfant_droit)
    return texte

def remplir_arbre(arbre : arbre_bianire):
    
    while(True):
        try:
            print("rappel tapper '00' pour terminer")
            valeur:int=int(input("entrer un nombre pour le noeud suivant"))
        except ValueError:
            print("entrer un chiffre")
        if valeur==00:
            break
        else:
            arbre.inserer_noeud(valeur)
            
        


if __name__ == '__main__':
    
    """---------------creation de l'arbre par Vassili et on affiche larbre,et le parcours infixe------------------- """
    arbre : arbre_bianire = arbre_bianire(100)
    arbre.inserer_noeud(80)
    arbre.inserer_noeud(90)
    arbre.inserer_noeud(60)
    arbre.inserer_noeud(70)
    arbre.inserer_noeud(45)
    arbre.inserer_noeud(8)
    arbre.inserer_noeud(9)
    arbre.inserer_noeud(10)
    print("parcours infixe --> " + parcours(arbre))
    print('\n'+"dessin arbre : ")
    print(arbre.afficher())
    
    
    """rechercher la valeur dans l'arbre"""
    try:
        valeur_a_chercher = int(input("rechercher une valeur svp "))
    except ValueError:
        print("faut chercher un nombre")
    
    print("resultat de la recherche de ",valeur_a_chercher,"--> ",rechercher(arbre,valeur_a_chercher))
    
    
    """------------------maintenant on l'utilisateur va creer son propre arbre---------------"""
    
    
    print("maintenant on va creer notre propre arbre !" + '\n')
    try:
        noeud_depart = int(input("entrer le nombre du 1er  noeud"))
    except ValueError:
        print("faut entrer un nombre")
    
    arbre_creer = arbre_bianire(noeud_depart)
    remplir_arbre(arbre_creer)
    
    print("parcours infixe --> " + parcours(arbre_creer))
    print('\n'+"dessin arbre : ")
    print(arbre_creer.afficher())
    
    try:
        valeur_a_chercher = int(input("rechercher une valeur svp "))
    except ValueError:
        print("faut chercher un nombre")
    
    print("resultat de la recherche de ",valeur_a_chercher,"--> ",rechercher(arbre_creer,valeur_a_chercher))
            
        
            
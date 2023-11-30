class rectangle():

    def __init__(self,largeur,longeur,nbrRectangles) :
        self.__largeur = largeur
        self.__longeur = longeur
        self.__nbrRectangles= nbrRectangles
#getters and setters 
    def getlargeur(self,):
        return self.__largeur
    def setlargeur(self):
        return self.__largeur
    
    def getlongeur(self,):
        return self.__longeur
    def setlongeur(self):
        return self.__longeur
#methodes
    def perimetre(self):
        return(self.getlargeur + self.getlongeur)*2
    def surface(self):
        return(self.getlargeur  * self.getlongeur)
    def Tostring(self):
       return("la largeur est :",self.getlargeur, "la longeur est :", self.getlongeur)
    def Equals(self,R):
        longeur1, longeur2 = self.getlargeur(), self.getlongeur()
        largeur1, largeur2 = R.getlargeur(), R.getlargeur()

    
        if longeur1==longeur2 and largeur1==largeur2 :
            return True
        else:
            return False
class parallelepipede(rectangle):
    __NbP = 0
    def _init_(self, largeur, longueur, hauteur):
        super()._init_(largeur, longueur)
        self.__hauteur = hauteur
        parallelepipede.__NbP = parallelepipede.__NbP + 1

#getters and setters 
    def gethauteur(self) :
        return self.__hauteur
    
    def sethauteur(self, hauteur) :
        self.__hauteur = hauteur
    
#methodes
    def surface(self):
        return 2 * (rectangle.getlargeur * rectangle.getlongueur + rectangle.getlongueur * parallelepipede.gethauteur + Rectangle.getlargeur * parallelepipede.gethauteur)
    
    def volume(self) :
        return rectangle.getlongueur * rectangle.getlargeur * parallelepipede.gethauteur
    
    def ToString(self):
        return super().ToString(), "la hauteur est :", parallelepipede.gethauteur
    
    def equals(self):
        hau1 = self.gethauteur
        hau2 = parallelepipede.gethauteur
        if hau1 == hau2 :
           return True
        else:
           return False
   
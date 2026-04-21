import abc

class Pizza(abc.ABC):
    def __init__(self, nom, *ingredients, prix) :
        self.__nom = nom
        self.__ingredients = list(ingredients)
        self.__prix = prix
    
    def get_nom(self) :
        return self.__nom

    def get_ingredients(self) :
        return self.__ingredients

    def get_prix(self) :
        return self.__prix
    
    def __str__(self) :
        return self.__nom + " : " + str(self.__ingredients) + " - " + str(self.__prix) + "€"

import CartePizzeriaException

class CartePizzeria:
    def __init__(self, *liste_pizzas) :
        self.__liste_pizzas = list(liste_pizzas)
    
    def is_empty(self) : 
        return len(self.__liste_pizzas) == 0

    def nb_pizzas(self) :
        return len(self.__liste_pizzas)
    
    def add_pizza(self, pizza) : 
        self.__liste_pizzas.apend(pizza)
    
    def remove_pizza(self, name) :
        for pizza in self.__liste_pizzas :
            if pizza.get_nom() == name:  
                self.__liste_pizzas.remove(pizza)
                return 
        raise CartePizzeriaException("Cette pizza n'est pas dans la carte")
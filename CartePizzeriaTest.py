import CartePizzeria, CartePizzeriaException
import pytest
from unittest.mock import MagicMock

class CartePizzeriaTest:

    def test_is_empty_True(self) :
        carte = CartePizzeria()
        assert carte.is_empty() == True

    def test_is_empty_False(self) :
        pizza = MagicMock()
        carte = CartePizzeria(pizza)
        assert carte.is_empty() == False
    
    def test_nb_pizzas_0(self) :
        carte = CartePizzeria()
        assert carte.nb_pizzas() == 0

    def test_nb_pizzas_1(self) :
        pizza = MagicMock()
        carte = CartePizzeria(pizza)
        assert carte.nb_pizzas() == 1   
        
    def test_nb_pizzas_2(self) :
        pizza1 = MagicMock()
        pizza2 = MagicMock()
        carte = CartePizzeria(pizza1, pizza2)
        assert carte.nb_pizzas() == 2

    def test_add_pizza(self) :
        pizza1 = MagicMock()
        pizza2 = MagicMock()
        carte = CartePizzeria(pizza1)
        carte.add_pizza(pizza2)
        assert carte.nb_pizzas() == 2

    def test_remove_pizza(self) :
        pizza1 = MagicMock()
        pizza1.get_nom.return_value = "Pizza1"
        pizza2 = MagicMock()
        pizza2.get_nom.return_value = "Pizza2"
        carte = CartePizzeria(pizza1, pizza2)
        carte.remove_pizza("Pizza1")
        assert carte.nb_pizzas() == 1
        with pytest.raises(CartePizzeriaException) :
            carte.remove_pizza("Pizza3")
    
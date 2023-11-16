"""Instantiating a Class"""

"""
This is where we initiate the class we defined in the classes.py. In other words, we're creating objects that belong to that class.
"""


#from <file_name>.<module_name> import <class_
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) #CONSTRUCTOR

#accessing/setting attributes
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

#printing out some values
#print("my_pizza: ")
print("Size Attributes:")
print(my_pizza.size)

print("Toppings:")
print(my_pizza.toppings)

#slas_pizza size "medium", 5 toppings, NOT GF
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(inp_pizza: Pizza) -> float:
    """Function Calculate Price of Pizza"""
    if inp_pizza.size == "large":
        price: float = 6.25
    else:
        price: float == 5.00
    price += .75 * inp_pizza.toppings
    if inp_pizza.gluten_free:
        price += 1.00
    return price

print(price(sals_pizza))
print(price(my_pizza))

#Calling price_method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings

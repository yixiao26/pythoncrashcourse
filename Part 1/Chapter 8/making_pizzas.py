import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

from pizza import make_pizza

make_pizza(18, "bbq chicken", "jalapenos", "pineapple")
make_pizza(10, "feta cheese")

from pizza import make_pizza as mp

mp(14, "sausage", "onions")
mp(12, "spinach", "tomatoes", "black olives")

import pizza as p

p.make_pizza(10, "feta cheese")

from pizza import *

make_pizza(20, "pepperoni", "mushrooms", "green peppers")

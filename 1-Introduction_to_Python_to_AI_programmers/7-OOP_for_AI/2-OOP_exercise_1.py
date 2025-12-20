# Unit tests to check your solution
from tests import run_tests
from shirt import Shirt

shirt_one = Shirt("red", "S", "long-sleeve", 25)
shirt_one.change_price(10)
print("Price of shirt one is ${}".format(shirt_one.discount(0.12)))
shirt_two = Shirt("orange", "L", "short-sleeve", 10)
total = shirt_one.price + shirt_two.price
total_discounted = shirt_one.discount(0.14) + shirt_two.discount(0.06)

run_tests(shirt_one, shirt_two, total, total_discounted)
print("All tests passed !")

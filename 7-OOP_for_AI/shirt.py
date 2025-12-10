# The shirt_exercise file, which you are currently looking at if you are reading this,
# has an exercise to help guide you through coding with an object in Python.

# Fill out the TODOs in each section of the Jupyter notebook. You can find a solution in the answer.py file.

# First, run this code cell below to load the Shirt class.

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)

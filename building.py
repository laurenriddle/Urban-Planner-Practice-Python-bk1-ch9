import datetime

# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.
class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name

# Create 5 building instances
eight_hundred_eighth = Building("800 8th Street", 8)
nine_hundred_nine = Building("900 9th Street", 11)
ten_hundred_ten = Building("1000 10th Street", 10)
seven_hundred_seven = Building("700 7th Street", 7)
six_hundred_six = Building("600 6th Street", 6)

# Have each one get purchased by a real estate magnate
eight_hundred_eighth.purchase("Monkey Chicken")
nine_hundred_nine.purchase("Caleb R.")
ten_hundred_ten.purchase("Magnate M.")
seven_hundred_seven.purchase("James J.")
six_hundred_six.purchase("Chicken Monkey")

# After purchased, construct each one
eight_hundred_eighth.construct()
nine_hundred_nine.construct()
ten_hundred_ten.construct()
seven_hundred_seven.construct()
six_hundred_six.construct()


# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example: 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.
print(f"{eight_hundred_eighth.address} was purchased by a {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed.date()} and has {eight_hundred_eighth.stories} stories.")

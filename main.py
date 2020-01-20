from Vehicle import Vehicle
# car

class Mazda_3(Vehicle):
    def __init__(self):
        # self.main_color = 0
        # self.maximum_occupancy = 0
        self.fuel_capacity = 0

    def drive(self):
        print("BrooooommMM!")

# gravel bike

class Fugi(Vehicle):
    def __init__(self):
        # self.main_color = 0
        # self.maximum_occupancy = 0
        self.bar_type = ""

    def drive(self):
        print("Just keep peddling....just keep peddling!")
    def stop(self):
        print("The sudden stop causes the rider to flip over the handle bar....")
    def turn(self, direction):
        print(f"The rider put up his {direction} arm up to signal a turn.")

# Jet

class FighterJet(Vehicle):
    def __init__(self):
        # self.main_color = 0
        # self.maximum_occupancy = 0
        self.max_range = 0

    def drive(self):
        print("BBBBBBBBBBBBBOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMM!!!!!!!")
    def stop(self):
        print("Stops on the runway and waiting to taxi to its parking spot.")

# tank

class Tank(Vehicle):
    def __init__(self):
        # self.main_color = 0
        # self.maximum_occupancy = 0
        self.max_range = 0

    def drive(self):
        print("RRRRRRUUUUUMMMMBBBBBLLLLLEEEEE")
    def turn(self, direction):
        print(f"The tank takes a {direction} and crushes multiple cars!")

# weird car

class Three_Wheeled(Vehicle):
    def __init__(self):
        # self.main_color = 0
        # self. maximum_occupancy = 0
        self.wheel_number = 0

    def drive(self):
        print("Daddy why does that car only have three wheels? What is with the door being the front anyway...right?")
    def stop(self):
        print("Seriously what is with the door on that thing...what is it a clown car?")



mazda_five_door = Mazda_3()
cross = Fugi()
f_sixteen = FighterJet()
abrams = Tank()
isetta = Three_Wheeled()

cross.drive()
mazda_five_door.drive()
f_sixteen.drive()
abrams.drive()
isetta.drive()


cross.turn("left")
cross.stop()

abrams.turn("right")

isetta.stop()

f_sixteen.stop()
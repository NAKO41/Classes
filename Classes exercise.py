class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
#my_rocket = Rocket()
#print("Rocket altitude:", my_rocket.y)#starts the rocket at original y

#my_rocket.move_up()
#print("Rocket altitude:", my_rocket.y)#icreases y by 1 to 1

#my_rocket.move_up()
#print("Rocket altitude:", my_rocket.y)#icreases y by 1 to 2

#my_rocket.move_up()
#print("Rocket altitude:", my_rocket.y)#icreases y by 1 to 3

#this will make the rocket move multiple spaces up until it has moved 10
#while my_rocket.y <= 10:
    #my_rocket.move_up()
    #print("Rocket altitude:", my_rocket.y)


# Create a fleet of 5 rockets, and store them in a list.
#my_rockets = []
#for x in range(0,5):
    #new_rocket = Rocket()
    #my_rockets.append(new_rocket)


# Show that each rocket is a separate object.
#for rocket in my_rockets:
    #print(rocket, end=" ")

#does the same thing as above
#my_rockets = [Rocket() for x in range(0,5)]


#move the first Rocket up only
#my_rockets[0].move_up()

#show that only the first rocket has moved.
#for rocket in my_rockets:
    print("altitude:" , rocket.y)















class FireBall(object):
    #this is the class object
    #it will be used to track weather an attack hits or not


    def __init__(self):
        #each ball will start at (0,0)

        self.y = 0
        self.x = 0

    def move_forward(self):
        self.x += 1

#create a fireball and make it move forward

fire_ball = FireBall()#creats a fireball and makes a variable = to the class

print(fire_ball)#prints a fire ball
print("the attack has moved", fire_ball.x, "spaces forwards")


fire_ball.move_forward()#this moves the fire ball
print("the attack has moved", fire_ball.x, "spaces forwards")

fire_ball.move_forward()#this moves the fire ball
print("the attack has moved", fire_ball.x, "spaces forwards")

#creat a barage of fireballs and store them in a list
fire_balls = []#creates an empty list
for i in range(5):
    #creates a fireball
    fire_balls.append(fire_ball)#adds the fireball to the list

for i in range(len(fire_balls)):#this loop wil print the list and make every item unique
            print(fire_ball, "fire ball", str(int(i + 1)))




             

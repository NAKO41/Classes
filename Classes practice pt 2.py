#this file is more focused on movements and starting objects at diffirent positions


class MDart():

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def move_up (self):
        self.y += 1

    def move_Dart(self, x_increment = 0, y_increment = 1):#the increments act as a default movement unless specified otherwise 
        self.x += x_increment
        self.y += y_increment


#this will make a list of Magic darts at diffirent starting positions
M_Darts = []
M_Darts.append(MDart())
M_Darts.append(MDart(10,40))
M_Darts.append(MDart(50,50))


#print the darts in their starting postions
for i in range(len(M_Darts)): 
    print("dart", str(int(i+1)), "starting location is", M_Darts[i].x, M_Darts[i].y)




#this will move each dart into a new position
M_Darts[0].move_Dart()#since no movements are spcified, the default movement will take place
M_Darts[1].move_Dart(10,10)
M_Darts[2].move_Dart(-10,0)


#print the new positions of the darts
for i in range(len(M_Darts)): 
    print("dart", str(int(i+1)), "new location is", M_Darts[i].x, M_Darts[i].y)

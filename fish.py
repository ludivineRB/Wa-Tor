# Class Fish Creation

class Fish(grid):

    def __init__(self, x_coordinate:int, y_coordinate:int) -> None:
        super().__init__(self, width, height, x_coordinate, y_coordinate, Reproductiontime)
        
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        
    def move(self, x, y, dir_x, dir_y):
        new_x = (x + dir_x) % self.width
        new_y = (y + dir_y) % self.height
        return new_x, new_y

# method move  
#    for fish in list_of_fish



    def move(self, list_of_animals):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

     """ for dir_x, dir_y in directions:
            new_x, new_y = Fish.move(self.x, self.y, dir_x, dir_y)
            empty = True
            for animals in list_of_animals:
                if animals.x == new_x and animals.y == new_y:
                    empty = False
                    break"""
        for dir_x in directions:
            new_x = Fish.move(self.x,dir)              



            if empty:
                x_old = fish.x_coordinate,
                y_old = fish.y_coordinate
                fish.x_coordinate = new_x, 
                fish.y_coordinate = new_y

    fish.ReproductionTime += 1




# method reproduction
# reproduction and initialization of the counter when greater than _
#    def reproduction(self):

#        if ReproductionTime > 6:
#            ReproductionTime = 0

#        else:
#            ReproductionTime += 1              
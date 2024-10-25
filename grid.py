class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def position(self, x, y):
        x % self.width
        y % self.height
        return (x,y)
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def position(self, x: int, y: int) -> tuple[int]:
        """
            Takes x and y coordinates and converts it to the torus planet

            args
            x coordinate which is an int
            y coordinate which is an int

            returns
            tuple of x and y coordinate
        """
        x = x % self.width
        y = y % self.height
        return (x,y)
class Grid:
    def __init__(self, width: int, height: int) -> None:
        """_summary_ creation of the class Grid

        Args:
            width (int): _description_
            height (int): _description_
        """
        self.width = width
        self.height = height
    
    def position(self, x: int, y: int) -> tuple[int]:
        """_summary_ converts coordinates

        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            tuple[int]: _description_
        """
        x = x % self.width
        y = y % self.height
        return (x,y)
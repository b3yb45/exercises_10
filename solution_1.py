class Circle:
    """
    This class represents a circle. It has two class attributes: 'all_circles' which
    is a list of all the Circle objects created and 'pi' which is a constant for the
    value of pi. Each instance of the class has one attribute: 'radius' which is the
    radius of the circle.
    """
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1.0):
        """
        Initializes a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle. If not provided, defaults to 1.0.

        Raises:
            ValueError: If the radius is negative.
            ValueError: If the radius cannot be converted to a float.
        """
        if radius <0:
            raise ValueError
        try:
            radius = float(radius)
        except:
            raise ValueError
        
        self.__radius = radius
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculates the area of the circle.
        """
        return Circle.pi * (self.__radius ** 2)
    
    @staticmethod
    def total_area():
        """
        Calculates the total area of all circles created.
        """
        total_area = 0
        for i in Circle.all_circles:
            total_area += i.area()

        return total_area
    
    def __str__(self):
        """
        Returns a string representation of the Circle object.
        """
        return f"Circle with radius {self.__radius}"
    
    def __repr__(self):
        """
        Returns a string representation of the Circle object.
        """
        return self.__str__()

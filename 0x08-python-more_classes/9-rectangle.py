#!/usr/bin/python3
"""
Class:
    Rectangle: Defines a rectangle.
"""


class Rectangle:
    """ class Rectangle that defines a rectangle object

    Attributes:
        __width: Width of the rectangle object
        __height: Height of the rectangle object
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize method that holds the height and width of a rectangle

        Args:
             width (int): Defines width of a rectangle
             height (int): Defines height of a rectangle
        """

        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """This method returns the width of a rectangle.
        """
        return (int(self.__width))

    @width.setter
    def width(self, value):
        """ Method to set the width value of the rectangle object

         Args:
            value (int): This defines the width of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This method returns the height of a rectangle.
        """
        return (int(self.__height))

    @height.setter
    def height(self, value):
        """ Method to set the height value of the rectangle object

         Args:
            value (int): This defines the height of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """This method returns the area of a rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """This method returns the perimeter of a rectangle."""
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """This method rturns a string that draws a recetngle."""
        if ((self.__width == 0) or (self.__height == 0)):
            return ("")

        draw_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                draw_str += str(self.print_symbol)
            if h != self.__height - 1:
                draw_str += "\n"
        return (draw_str)

    def __repr__(self):
        """This method returns a formal version of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """This method is a destructor
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the biggest rectangle based on error

        Args:
            rect_1: First rectangle
            rect_2: Second rectangle

        Returns:
            The bigger rectangle, or rect_1 if both are equal

        Raises:
            TypeError: When arguments are not of type Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """This method returns a new square.

        Args:
            size: The size value of the square

        Returns: A new square

        """
        return cls(size, size)

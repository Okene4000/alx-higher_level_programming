#!/usr/bin/python3
"""Define class with rectangles.
"""


class Rectangle:
    """Represents rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieve the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width has to be an integer')
        elif value < 0:
            raise ValueError('width has to be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Update the height of this Rectangle.
        Args:
            value (int): Get the new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height has to be an integer')
        elif value < 0:
            raise ValueError('height has to be >= 0')
        else:
            self.__height = value

    def area(self):
        """gives the area of this Rectangle.
        Returns:
            int: The area of this Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """gives the perimeter of this Rectangle.
        Returns:
            int: The perimeter of this Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the Rectangle.
        Returns:
            str: A string representation of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)


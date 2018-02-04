class Square:

    def __init__(self, height="0", width="0"):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        print("setting the height")
        if value.isdigit():
            self.__height = value
        else:
            print("Only enter float values")

    @property
    def width(self):
        print("Retrieving the widht")
        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only values")

    def getArea(self):
        return int(self.__height) * int(self.__width)


def main():
    aSquare = Square()

    userHeight = input("Enter the height: ")
    userWidth = input("Enter the width: ")

    aSquare.height = userHeight
    aSquare.width = userWidth

    print(" Height is :", aSquare.height)
    print(" Width is :", aSquare.width)

    print(" Area of square is :", aSquare.getArea())


main()
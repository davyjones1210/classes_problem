# Write a class definition for an Image.

sample_image = """
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
"""


class PracticeImage:

    # Implement as public functions the constructor,
    def __init__(self):
        # An Image object holds pixel values in a 10x10 grid.
        self._grid_size = 10
        self._pixel_values = [[] for i in range(self._grid_size)]

        # The pixels can either be on (using #) or off (using empty space).

        # The class should use private member variables for the symbol and pixels,
        self._pixel_status = False
        self._pixel_symbol = "#"
        self._output_string = ""

        # The double underscore __ prefixed to a variable makes it private.
        # It gives a strong suggestion not to touch it from outside the class.
        # Any attempt to do so will result in an AttributeError



    # getters and setters for the pixels and symbol,

    @property
    def pixel_info(self):
        """
            Getter function which simply returns the size and symbol for the pixels

                Parameters:
                    size and symbol for the pixels

                Returns:
                    size and symbol for the pixels
        """
        print("Getting the pixels info")
        print(
            f"Pixel values are: {self._pixel_values}, Pixel status is {self._pixel_status} & pixel symbol is {self._pixel_symbol}")
        print(f"Grid size is {self._grid_size}")
        return self._pixel_values, self._pixel_status, self._pixel_symbol, self._grid_size

    @pixel_info.setter
    def pixel_info(self, value: tuple) -> None:
        """
            Sets the symbol fon the pixels

                Parameters:
                    value: Tuple

                Returns:
                    None
        """
        print("Setting the pixels attributes")
        xPos, yPos, symbol = value
        self._pixel_values[xPos][yPos] = symbol




    # along with an output function
    def output_image(self):
        for i in range(self._grid_size):
            for j in range (self._grid_size):
                self._output_string += str(self._pixel_values[i][j])
            self._output_string += "\n"

        return self._output_string

    # and two image manipulation functions;
    # flip (horizontal mirror) and flop (vertical mirror).
    def flip(self):
        pass

    def flop(self):
        pass

    # as well as a fill function which should fill the image with empty pixels.
    def fill(self):

        for list in self._pixel_values:
            for i in range(self._grid_size):
                list.append(i)



def main():
    # Initializing the image object
    image_object = PracticeImage()

    image_object.fill()
    # Gets the pixels & symbols
    print("First get")
    print(image_object.pixel_info)

    # As a test, output an empty image
    #print(image_object.output_image())



    image_object.pixel_info = (0,0,'#')
    # Gets the pixels & symbols
    print("Second get")
    print(image_object.pixel_info)
    print(image_object.output_image())


    pass


# main entry point to the program
if __name__ == "__main__":
    main()

# Test the object by setting the first pixel at position 0,0 with the flip/flop functions.

# Can you implement a child class called Triangle that draws a right angle triangle?
# Overload the fill() function and test it with flip/flop functions from the base class.

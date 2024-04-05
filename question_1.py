# import numpy as np
# Write a class definition for an Image.

class PracticeImage:
    # Implement as public functions the constructor,
    def __init__(self):
        # An Image object holds pixel values in a 10x10 grid.
        self._grid_size = 10
        self._pixel_values = [[] for i in range(self._grid_size)]

        # The pixels can either be on (using #) or off (using empty space).

        # The class should use private member variables for the symbol and pixels,
        self._pixel_symbol = "#"
        self._pixel_off_symbol = " "
        self._output_string = ""

        # Not keeping the original so removing these extra variables
        # self._flipped_values = [[] for i in range(self._grid_size)]
        # self._flipped_output_string = ""
        # self._flopped_values = [[] for i in range(self._grid_size)]
        # self._flopped_output_string = ""
        # self._incoming_pixel_values = [[] for i in range(self._grid_size)]

    # getters and setters for the pixels and symbol,
    @property
    def pixel_info(self):
        """
        Getter function which simply returns the size and symbol for the pixels

        Args:
            None

        Returns:
            Tuple: list of Pixel values, str of pixel symbol, int of grid size, str of pixel off symbol
        """
        # print("Getting the pixels info") print( f"Pixel values are: {self._pixel_values}, Pixel status is {
        # self._pixel_status} & pixel symbol is {self._pixel_symbol}") print(f"Grid size is {self._grid_size}")

        return self._pixel_values, self._pixel_symbol, self._grid_size, self._pixel_off_symbol

    @pixel_info.setter
    def pixel_info(self, value: tuple) -> None:
        """
        Setter function which Sets the symbol for the pixels

        Args:
        value (tuple): Passed from the main function are the pixel position and symbol

        Returns:
            None
        """
        # print("Setting the pixels attributes")
        xPos, yPos, symbol = value
        self._pixel_values[xPos][yPos] = symbol

    # along with an output function
    def output_image(self):
        """
        Converts the pixel values stored in the image object to string and prints the string

        Args:
            None

        Returns:
            None
        """

        self._output_string = ""
        for i in range(self._grid_size):
            for j in range(self._grid_size):
                self._output_string += str(self._pixel_values[i][j])
            self._output_string += "\n"

        print(self._output_string)

    # and two image manipulation functions; flip (horizontal mirror) and flop (vertical mirror).
    def flip(self) -> None:
        """
        Make a horizontal mirror of the pixel values referenced in the image object.

        Args:
            None

        Returns:
            None
        """

        self._pixel_values = self._pixel_values[::-1]


    def flop(self) -> None:
        """
            Make a vertical mirror of the pixel values referenced in the image object.

            Args:
                None

            Returns:
                None
        """
        # result = [x[::-1] for x in myl]
        self._pixel_values = [x[::-1] for x in self._pixel_values]

    # as well as a fill function which should fill the image with empty pixels.
    def fill(self):
        """
             Fills the image with empty pixels as a way to clear all pixel values

            Args:
                None

            Returns:
                None
        """
        for list in self._pixel_values:
            for i in range(self._grid_size):
                list.append(self._pixel_off_symbol)


# Can you implement a child class called Triangle that draws a right angle triangle?
class Triangle(PracticeImage):
    # child class called Triangle that draws a right angle triangle

    def __init__(self):
        super().__init__()
        self._triangle_output_string = ""

    def draw_right_angle_triangle(self, symbol: str):
        """
         Draws a right-angled triangle on a 10x10 grid using the symbol passed from the main function

        Parameters:
            symbol (str): The symbol which will be filled in the pixel values to create a right-angled triangle

        Returns:
            None
        """
        for i in range(self._grid_size):
            self._pixel_values[i][0] = symbol
            for j in range(self._grid_size):
                self._pixel_values[self._grid_size - 1][j] = symbol
                if i == j:
                    self._pixel_values[i][j] = symbol
        self.output_image()


def main():
    # Initializing the image object
    image_object = PracticeImage()
    # print(type(image_object))
    image_object.fill()

    # Calling first setter function to set pixel values and symbol
    # Test the object by setting the first pixel at position 0,0 with the flip/flop functions.
    image_object.pixel_info = (0, 0, '#')
    # Calling the getter which gets the pixels & symbols
    # print("Testing get function ")
    # print(image_object.pixel_info)
    print("Testing the object by setting the first pixel at position 0,0 with the flip/flop functions:")
    image_object.output_image()
    # print(image_object.output_image())
    print("Flip")
    image_object.flip()
    image_object.output_image()

    # print('Flipped output image')
    # print(flipped_output)
    print("Flop")
    image_object.flop()
    image_object.output_image()
    # print('Flopped output image')
    # print(flopped_output)

    # Making right angled triangle

    right_angled_triangle = Triangle()

    # Overload the fill() function and test it with flip/flop functions from the base class.
    right_angled_triangle.fill()

    # As a test, output an empty image
    print("Test output from drawing right angled triangle")
    print(right_angled_triangle.draw_right_angle_triangle('#'))

    print("Test right angled triangle flip")
    right_angled_triangle.flip()
    right_angled_triangle.output_image()
    # print(right_angled_triangle.flip())
    print("Test right angled triangle flop")
    right_angled_triangle.flop()
    right_angled_triangle.output_image()
    # print(right_angled_triangle.flop())


# main entry point to the program
if __name__ == "__main__":
    main()






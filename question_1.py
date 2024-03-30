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
        self._pixel_status = False
        self._pixel_symbol = "#"
        self._output_string = ""
        self._flipped_values = [[] for i in range(self._grid_size)]
        self._flipped_output_string = ""
        self._flopped_values = [[] for i in range(self._grid_size)]
        self._flopped_output_string = ""


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
        #print("Getting the pixels info")
        # print(
        #    f"Pixel values are: {self._pixel_values}, Pixel status is {self._pixel_status} & pixel symbol is {self._pixel_symbol}")
        # print(f"Grid size is {self._grid_size}")
        return self._pixel_values, self._pixel_status, self._pixel_symbol, self._grid_size

    @pixel_info.setter
    def pixel_info(self, value: tuple) -> None:
        """
            Sets the symbol fon the pixels

                Parameters:
                    value: Tuple passed from the main funciton are the pixel number and symbol

                Returns:
                    None
        """
        #print("Setting the pixels attributes")
        xPos, yPos, symbol = value
        self._pixel_values[xPos][yPos] = symbol

    # along with an output function
    def output_image(self):
        """
            Converts the pixel values stored in the image object to string and returns the string

                Parameters:
                    None

                Returns:
                    Output image in str format readable on the console.
        """
        for i in range(self._grid_size):
            for j in range (self._grid_size):
                self._output_string += str(self._pixel_values[i][j])
            self._output_string += "\n"

        return self._output_string

    # and two image manipulation functions;
    # flip (horizontal mirror) and flop (vertical mirror).
    def flip(self) -> str:
        """
            Make a horizontal mirror of the pixel values referenced in the image object.

                Parameters:
                    None

                Returns:
                    Output image of the horizontal mirror in str format readable on the console,
                    without affecting the original pixel values.
        """
        self._flipped_values = self._pixel_values[::-1]
        # print("Manual horizontal flip")
        # print(self._flipped_values)

        for i in range(self._grid_size):
            for j in range (self._grid_size):
                self._flipped_output_string += str(self._flipped_values[i][j])
            self._flipped_output_string += "\n"

        return self._flipped_output_string

    def flop(self) -> str:
        """
            Make a vertical mirror of the pixel values referenced in the image object.

                Parameters:
                    None

                Returns:
                    Output image of the vertical mirror in str format readable on the console,
                    without affecting the original pixel values.
        """
        # result = [x[::-1] for x in myl]
        self._flopped_values = [x[::-1] for x in self._pixel_values]

        # print("Manual Vertical flop")
        # print(self._flopped_values)

        for i in range(self._grid_size):
            for j in range(self._grid_size):
                self._flopped_output_string += str(self._flopped_values[i][j])
            self._flopped_output_string += "\n"

        return self._flopped_output_string


    # as well as a fill function which should fill the image with empty pixels.
    def fill(self):
        """
            Fill the entire pixel array with black spaces as a way to clear all pixel values

                Parameters:
                    None

                Returns:
                    None
        """
        for list in self._pixel_values:
            for i in range(self._grid_size):
                list.append(' ')

class Triangle(PracticeImage):
    # child class called Triangle that draws a right angle triangle

    def __init__(self):
        super().__init__()
        self._triangle_output_string = ""

    def draw_right_angle_triangle(self, symbol):

        for i in range(self._grid_size):
            self._pixel_values[i][0] = symbol
            for j in range(self._grid_size):
                self._pixel_values[self._grid_size-1][j] = symbol
                if i == j:
                    self._pixel_values[i][j] = symbol

        for i in range(self._grid_size):
            for j in range(self._grid_size):
                self._triangle_output_string += str(self._pixel_values[i][j])
            self._triangle_output_string += "\n"

        return self._triangle_output_string

        pass

def main():
    # Initializing the image object
    image_object = PracticeImage()
    #print(type(image_object))
    image_object.fill()
    # Gets the pixels & symbols
    #print("First get")
    #print(image_object.pixel_info)

    # As a test, output an empty image
    #print(image_object.output_image())
    # getting_image_info = image_object.pixel_info

    # Calling first setter function to set pixel values and symbol
    image_object.pixel_info = (0,0,'#')
    # Gets the pixels & symbols
    # print("Second get")
    print(image_object.pixel_info)
    print("Output image:")
    print(image_object.output_image())
    flipped_output = image_object.flip()
    print('Flipped output image')
    print(flipped_output)

    flopped_output = image_object.flop()
    print('Flopped output image')
    print(flopped_output)

    # Making right angled triangle

    right_angled_triangle = Triangle()
    right_angled_triangle.fill()

    # As a test, output an empty image
    print("Test output from drawing right angled triangle")
    print(right_angled_triangle.draw_right_angle_triangle('#'))

    print("Test right angled triangle flip")
    print(right_angled_triangle.flip())
    print("Test right angled triangle flop")
    print(right_angled_triangle.flop())








# main entry point to the program
if __name__ == "__main__":
    main()

# Test the object by setting the first pixel at position 0,0 with the flip/flop functions.

# Can you implement a child class called Triangle that draws a right angle triangle?
# Overload the fill() function and test it with flip/flop functions from the base class.

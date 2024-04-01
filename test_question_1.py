from question_1 import PracticeImage
from question_1 import Triangle
import unittest
import numpy as np

# pytest test_question_1.py --cov-report term-missing --cov -v
sample_triangle_image = """#         
##        
# #       
#  #      
#   #     
#    #    
#     #   
#      #  
#       # 
##########
"""
# python -m unittest discover


class TestPixels(unittest.TestCase):
    # tests go here
    # python -m unittest test_question_1.TestPixels.test_if_variables_are_initialized_correctly
    def test_if_variables_are_initialized_correctly(self):
        test_image_object = PracticeImage()
        self.assertEqual(test_image_object._grid_size, 10)

    # python -m unittest test_question_1.TestPixels.test_if_getter_method_returns_values
    def test_if_getter_method_returns_values(self):
        test_image_object = PracticeImage()
        self.assertIsNotNone(test_image_object.pixel_info)

    # python -m unittest test_question_1.TestPixels.test_if_setter_method_sets_values
    def test_if_setter_method_sets_values(self):
        test_image_object = PracticeImage()
        test_image_object.fill()
        test_image_object.pixel_info = (0, 0, '#')
        self.assertEqual(test_image_object._pixel_values[0][0], '#')

    # python -m unittest test_question_1.TestPixels.test_if_output_image_returns_10x10_image
    def test_if_output_image_returns_10x10_image(self):
        test_image_object = PracticeImage()
        test_image_object.fill()
        image_string = test_image_object.output_image()
        self.assertEqual(len(image_string), 110)

    # python -m unittest test_question_1.TestPixels.test_flip_method_works
    def test_flip_method_works(self):
        test_numpy_string = ""
        test_image_object = PracticeImage()
        test_image_object.fill()
        test_getting_image_info = test_image_object.pixel_info
        test_image_object.pixel_info = (0, 0, '#')
        flipped_test_image = test_image_object.flip()

        numpy_flipped_image = np.flip(test_getting_image_info[0], 0)
        # new_numpy_image = list(map(int, numpy_flipped_image))
        # print("Manual image")
        # print(test_getting_image_info[0])

        # print("Manual string")
        test_output_string = test_image_object.output_image()
        # print(test_output_string)

        # print("Manual flipped string")
        # print(flipped_test_image)

        # print("Numpy flipped list image")
        list_numpy_flipped_image = numpy_flipped_image.tolist()
        # print(list_numpy_flipped_image)
        for i in range(test_image_object._grid_size):
            for j in range(test_image_object._grid_size):
                test_numpy_string += str(list_numpy_flipped_image[i][j])
            test_numpy_string += "\n"

        # print("Numpy flipped string")
        # print(test_numpy_string)
        self.assertEqual(flipped_test_image, test_numpy_string)

    # python -m unittest test_question_1.TestPixels.test_flop_method_works
    def test_flop_method_works(self):
        test_numpy_string = ""
        test_image_object = PracticeImage()
        test_image_object.fill()
        test_getting_image_info = test_image_object.pixel_info
        test_image_object.pixel_info = (0, 0, '#')
        flopped_test_image = test_image_object.flop()
        # myl_flip_v = np.flip(myl,1) # vertical flip
        numpy_flopped_image = np.flip(test_getting_image_info[0], 1)
        # new_numpy_image = list(map(int, numpy_flopped_image))
        # print("Manual image")
        # print(test_getting_image_info[0])

        # print("Manual string")
        test_output_string = test_image_object.output_image()
        # print(test_output_string)

        # print("Manual flopped string")
        # print(flopped_test_image)

        # print("Numpy flipped list image")
        list_numpy_flopped_image = numpy_flopped_image.tolist()
        # print(list_numpy_flipped_image)
        for i in range(test_image_object._grid_size):
            for j in range(test_image_object._grid_size):
                test_numpy_string += str(list_numpy_flopped_image[i][j])
            test_numpy_string += "\n"

        # print("Numpy flopped string")
        # print(test_numpy_string)
        self.assertEqual(flopped_test_image, test_numpy_string)

    # python -m unittest test_question_1.TestPixels.test_if_triangle_variables_are_initialized_correctly
    def test_if_triangle_variables_are_initialized_correctly(self):
        test_right_angled_triangle = Triangle()
        self.assertEqual(test_right_angled_triangle._triangle_output_string, '')

    # python -m unittest test_question_1.TestPixels.test_draw_right_angle_triangle_works
    def test_draw_right_angle_triangle_works(self):
        test_right_angled_triangle = Triangle()
        test_right_angled_triangle.fill()
        test_output_triangle = test_right_angled_triangle.draw_right_angle_triangle('#')
        # print("Test output of triangle")
        # print(test_output_triangle)
        # print('Sample triangle image')
        # print(sample_triangle_image)
        self.assertEqual(test_output_triangle, sample_triangle_image)



    if __name__ == "__main__":
        unittest.main()
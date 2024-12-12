import unittest
from area import circle, square, rectangle, triangle


class TestAreaFunctions(unittest.TestCase):

    def test_circle(self):
        """Test the circle area function."""
        # Test with a positive radius
        self.assertAlmostEqual(circle(5), 78.53975, places=5)  # area of circle with radius 5
        self.assertAlmostEqual(circle(0.5), 0.7853975, places=7)  # area of circle with radius 0.5

        # Test with invalid input (negative radius)
        with self.assertRaises(ValueError) as context:
            circle(-5)
        self.assertEqual(str(context.exception), "Radius must be positive.")  # Assuming your function raises this error

        # Test with invalid input (non-numeric)
        with self.assertRaises(TypeError) as context:
            circle("abc")
        self.assertEqual(str(context.exception), "Input must be a number.")

    def test_square(self):
        """Test the square area function."""
        # Test with a valid positive side length
        self.assertEqual(square(4), 16)
        self.assertEqual(square(0.5), 0.25)

        # Test with invalid input (negative side length)
        with self.assertRaises(ValueError) as context:
            square(-3)
        self.assertEqual(str(context.exception), "Side length must be positive.")

        # Test with invalid input (non-numeric)
        with self.assertRaises(TypeError) as context:
            square("xyz")
        self.assertEqual(str(context.exception), "Input must be a number.")

    def test_rectangle(self):
        """Test the rectangle area function."""
        # Test with valid side lengths
        self.assertEqual(rectangle(4, 5), 20)
        self.assertEqual(rectangle(0.5, 2), 1)

        # Test with invalid input (negative length)
        with self.assertRaises(ValueError) as context:
            rectangle(-4, 5)
        self.assertEqual(str(context.exception), "Length and width must be positive.")

        # Test with invalid input (non-numeric)
        with self.assertRaises(TypeError) as context:
            rectangle("abc", 3)
        self.assertEqual(str(context.exception), "Length and width must be numbers.")

    def test_triangle(self):
        """Test the triangle area function."""
        # Test with valid base and height
        self.assertEqual(triangle(4, 5), 10)
        self.assertEqual(triangle(0.5, 2), 0.5)

        # Test with invalid input (negative base or height)
        with self.assertRaises(ValueError) as context:
            triangle(-3, 4)
        self.assertEqual(str(context.exception), "Base and height must be positive.")

        # Test with invalid input (non-numeric)
        with self.assertRaises(TypeError) as context:
            triangle(4, "xyz")
        self.assertEqual(str(context.exception), "Base and height must be numbers.")


if __name__ == "__main__":
    unittest.main()

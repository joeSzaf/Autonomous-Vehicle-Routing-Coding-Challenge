import unittest

from generate_grid import generate_grid

class myTest(unittest.TestCase):
    def test_generate_grid(self):
        # check to see if given a non-valid grid size
        self.assertEqual( isinstance(generate_grid(0, 5), str), True )
        self.assertEqual( isinstance(generate_grid(9, -2), str), True )

        # tests if grid generates the correct number of rows
        self.assertEqual( length(generate_grid(10, 10)), 10 )


unittest.main()

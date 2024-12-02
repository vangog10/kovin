import unittest
import main


class MyTestCase(unittest.TestCase): #glazyrina
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__': #konstantinova
    unittest.main()

from __future__ import print_function
import unittest
import roadrunner


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import roadrunner.testing

        roadrunner.testing.runTester()
        # TODO: check the return value of the tester (how many failed)
        self.assertTrue(roadrunner.__version__.startswith("1.4.1"))


if __name__ == '__main__':
    unittest.main()

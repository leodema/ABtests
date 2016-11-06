import unittest

from ABtests.stats import z_test


class TestZTest(unittest.TestCase):
    def test_prop_st(self):
        res = z_test(3, 10, 0.3)
        self.assertEqual(res, (0, 0.5))

    def test_prop_st(self):
        res = z_test(1, 10, 0.1)
        self.assertEqual(res, (0, 0.5))

if __name__ == '__main__':
    unittest.main()
import unittest


class LisiTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_lisi1(self):
        self.assertEqual(2, 2)
    def test_lisi1(self):
        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()

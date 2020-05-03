import unittest


class WanguuTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertNotEqual(True, False)


if __name__ == '__main__':
    unittest.main()

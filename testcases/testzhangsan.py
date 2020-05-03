import unittest
from lib import ssh


class ZhangsanTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_zhangsan1(self):
        res = ssh.ssh_execmd("xxx", "xxxxx", "echo hello")
        self.assertEqual(res.replace("\n",""), "hello")

    def test_zhangsan2(self):
        self.assertEqual(5,5)


if __name__ == '__main__':
    unittest.main()

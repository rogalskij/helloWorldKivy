import unittest

from DataModel.skill import Skill


class TestReturnlvl(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        s0 = Skill(0)
        s3 = Skill(3)
        s4 = Skill(4)
        s1000 = Skill(1000)
        self.assertEqual(s0.return_lvl(), 0)
        self.assertEqual(s3.return_lvl(), 0)
        self.assertEqual(s4.return_lvl(), 1)
        self.assertEqual(s1000.return_lvl(), 9)

if __name__ == '__main__':
    unittest.main()
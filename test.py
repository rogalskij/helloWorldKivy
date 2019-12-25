import unittest

from DataModel.skill import Skill


class TestSkill(unittest.TestCase):

    def test_skill_int(self):
        """
        Test that it can sum a list of integers
        """
        s0 = Skill(0)
        s3 = Skill(3)
        s4 = Skill(4)
        s1000 = Skill(1000)
        self.assertEqual(s3.value, 3)
        self.assertEqual(s0.return_lvl(), 0)
        self.assertEqual(s3.return_lvl(), 0)
        self.assertEqual(s4.return_lvl(), 1)
        self.assertEqual(s1000.return_lvl(), 9)
        self.assertEqual(s1000.current_lvl, 9)

    def test_skill_train(self):
        """
        Test that it can sum a list of integers
        """
        s0 = Skill(0)
        s3 = Skill(3)

        s0.train(1)
        s3.train(1)

        self.assertEqual(s0.value, 1)
        self.assertEqual(s3.value, 4)
        self.assertEqual(s0.return_lvl(), 0)
        self.assertEqual(s3.return_lvl(), 1)




if __name__ == '__main__':
    unittest.main()
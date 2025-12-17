import unittest

from bowling.bowling import Bowling


class BowlingTest(unittest.TestCase):
    def setUp(self):
        self.bowling = Bowling()

    def tearDown(self):
        self.bowling = None

    def test_should_return_0_after_all_failed_rolls(self):
        self.roll_many(0)
        self.assertEqual(0, self.bowling.get_score())

    def test_should_return_20_for_all_ones(self):
        self.roll_many(1)
        self.assertEqual(20, self.bowling.get_score())

    def test_should_add_bonus_after_spare(self):
        self.bowling.roll(7)
        self.bowling.roll(3)
        self.bowling.roll(2)
        for i in range(17):
            self.bowling.roll(0)
        self.assertEqual( 14, self.bowling.get_score())

    def test_should_add_bonus_after_strike(self):
        self.bowling.roll(10)
        self.bowling.roll(1)
        self.bowling.roll(2)
        for i in range(16):
            self.bowling.roll(0)
        self.assertEqual( 16, self.bowling.get_score())

    def test_should_add_bonus_after_strike_at_the_end(self):
        for i in range(16):
            self.bowling.roll(0)
        self.bowling.roll(10)
        self.bowling.roll(1)
        self.bowling.roll(2)
        self.assertEqual( 16, self.bowling.get_score())

    def test_should_return_perfect_score(self):
        for i in range(12):
            self.bowling.roll(10)
        self.assertEqual( 300, self.bowling.get_score())







    def roll_many(self, pins):
        for i in range(20):
            self.bowling.roll(pins)







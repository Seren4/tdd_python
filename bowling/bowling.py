TOTAL_FRAMES = 10


class Bowling():
    score = []

    def __init__(self):
        self.score = []

    def get_score(self):
        result = 0
        index = 0
        for frame in range(TOTAL_FRAMES):
            if self.is_strike(index):
                result += self.strike_bonus(index)
                result += 10
                index+=1
                continue

            if self.is_spare(index):
                result += self.spare_bonus(index)
            result += self.frame_score(index)
            index+=2

        return result

    def strike_bonus(self, index):
        return self.score[index + 1] + self.score[index + 2]

    def is_strike(self, index):
        return self.score[index] == 10

    def spare_bonus(self, index):
        return self.score[index + 2]

    def is_spare(self, index):
        return self.frame_score(index) == 10

    def frame_score(self, index):
        return self.score[index] + self.score[index + 1]

    def roll(self, pins):
        self.score.append(pins)
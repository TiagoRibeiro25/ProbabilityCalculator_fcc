# Imports
import random
import copy


class Hat:
    def __init__(self, **hats):
        self.contents = [k for k, v in hats.items() for _ in range(v)]

    def draw(self, n):
        """
        We're going to pop n items from the deck, but we're going to pop them randomly.

        :param n: the number of cards to draw
        :return: A list of n random elements from the deck.
        """

        n = min(n, len(self.contents))

        return [
            self.contents.pop(
                random.randrange(len(self.contents))
            ) for _ in range(n)
        ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    It runs a simulation of drawing balls from a hat, and returns the probability of drawing the
    expected balls.

    :param hat: a list of balls in the hat
    :param expected_balls: a dictionary of the balls you want to draw and the number of times you want
    to draw them
    :param num_balls_drawn: The number of balls drawn from the hat
    :param num_experiments: The number of times you want to run the experiment
    :return: The probability of drawing the expected balls from the hat.
    """

    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)

        balls_req = sum([
            1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v
        ])

        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments

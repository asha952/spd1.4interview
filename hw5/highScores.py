"""
Manage a game player's High Score list.

Your task is to build a high-score component of the classic
Frogger game, one of the highest selling and addictive games
of all time, and a classic of the arcade era. Your task is
to write methods that return the highest score from the list,
the last added score and the three highest scores.

In this exercise, you're going to use and manipulate lists.
Python lists are very versatile, and you'll find yourself
using them again and again in problems both simple and complex.

"""
sample_scores = [100, 500, 210, 110, 9000, 50, 700]


def highScore(scores):  # returns highest score
    return max(scores)


def addedScore(scores):
    sum_scores = 0
    for each_score in scores:
        sum_scores = each_score + sum_scores
    return sum_scores


def top_threeScores(scores):
    return sorted(scores, reverse=True)[0:3]


# print(highScore(sample_scores))
# print(addedScore(sample_scores))
print(top_threeScores(sample_scores))

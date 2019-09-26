# pythonds - Programming Exercises - (#1)
# Based on https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Exercises.html
# Devise an experiment to verify that the list index operator is O(1)

from timeit import Timer
import random

def test(l, idx):
    return l[idx]

listIndex = Timer("test(x, r)", "from __main__ import test, x, r")

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    r = random.randint(1, i - 1)
    tt = listIndex.timeit(number=1000)
    print("for list of size %d it took %15.5f to get x[%d]" %(i, tt, r))

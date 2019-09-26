# pythonds - Programming Exercises - (#2)
# Based on https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Exercises.html
# Devise an experiment to verify that get item and set item are O(1) for dictionaries

from timeit import Timer
import random

print("size get set")
for i in range(1000000, 100000001, 1000000):
    getItem = Timer("y = x[random.randint(0, i - 1)]", "from __main__ import random, x, i")
    setItem = Timer("x[random.randint(0, i - 1)] = i", "from __main__ import random, x, i")

    x = {j: None for j in range(i)}

    getItemTime = getItem.timeit(number=1000)
    setItemTime = setItem.timeit(number=1000)

    print("%d   %15.5f  %15.5f" % (i, getItemTime, setItemTime))

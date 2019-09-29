# pythonds - Programming Exercises - (#3)
# Based on https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Exercises.html
# Devise an experiment that compares the performance of the del operator on lists and dictionaries

from timeit import Timer
import random

print("%7s %15s %15s" % ("size", "list", "dictionary"))

for i in range(1000000, 100000001, 1000000):
    listDelOperation = Timer("del l[candidateListIndexes.pop()]", "from __main__ import l, candidateListIndexes")
    dictDelOperation = Timer("del d[candidateDictKeys.pop()]", "from __main__ import d, candidateDictKeys")

    l = list(range(i))
    candidateListIndexes = [random.randint(0, len(l) - j) for j in range(1000, 0, -1)]
    delOnListTime = listDelOperation.timeit(number=1000)

    d = {k: None for k in range(i)}
    dictKeys = list(d.keys())
    random.shuffle(dictKeys)
    candidateDictKeys = dictKeys[:1000]
    delOnDictTime = dictDelOperation.timeit(number=1000)

    print("%7d %15.5f %15.5f" % (i, delOnListTime, delOnDictTime))

# pythonds - Programming Exercises - (#4)
# Based on https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/Exercises.html
# Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list

def findKthSmallestNumber(listOfNumber, k):
    listOfNumber.sort()

    return listOfNumber[k - 1]


print(findKthSmallestNumber([9, 10, 2, 6, 1, 7, 8, 3, 4, 5], 5))  # should print 5
print(findKthSmallestNumber([29, 15, 22, 46, 11, 37], 3))  # should print 22
print(findKthSmallestNumber([-91, 15, -22, 36, 11, 37, -8, -13], 7))  # should print 36

# pythonds - Big-O Notation - Self Check (#1)
# Based https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/BigONotation.html
# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n).

# of O(n2)
def findMin1(numbers):
    for currentNumber in numbers:
        isMin = True
        for theOtherNumber in numbers:
            if theOtherNumber == currentNumber:
                continue
            isMin = isMin and currentNumber <= theOtherNumber
        if isMin:
            return currentNumber

# of O(n)
def findMin2(numbers):
    candidateMin = numbers[0]
    for currentNumber in numbers[1:]:
        if currentNumber < candidateMin:
            candidateMin = currentNumber
    return candidateMin

print(findMin1([2,3,6,1,-1,0,-2]))
print(findMin2([2,3,6,1,-1,0,-2]))

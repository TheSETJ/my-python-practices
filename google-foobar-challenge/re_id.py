# Google foo.bar code challenge
#
# Re-ID
# =====
#
# There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been
# lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has 
# tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 
#
# She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a 
# number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will 
# be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 
#
# Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of 
# Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of 
# minions, so the value of n will always be between 0 and 10000. 
#
# Languages
# =========
#
# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Java cases --
# Input:
# Solution.solution(0)
# Output:
#     23571
#
# Input:
# Solution.solution(3)
# Output:
#     71113
#
# -- Python cases --
# Input:
# solution.solution(0)
# Output:
#     23571
#
# Input:
# solution.solution(3)
# Output:
#     71113
#
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit 
# [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder. 

import math

idDigitCount = 5


# borrowed from: https://www.geeksforgeeks.org/program-to-find-the-next-prime-number/
def isPrime(number):
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number) + 1), 6):
        if (number % i) == 0 or (number % (i + 2)) == 0:
            return False

    return True


# borrowed from: https://www.geeksforgeeks.org/program-to-find-the-next-prime-number/
def nextPrime(number):
    if number <= 1:
        return 2

    prime = number
    found = False

    while not found:
        prime = prime + 1

        if isPrime(prime) == True:
            found = True

    return prime


def makePrimeString(preferedLength):
    primeNumber = 2
    primeString = ''

    while len(primeString) < preferedLength:
        primeString += str(primeNumber)
        primeNumber = nextPrime(primeNumber)

    return primeString


def solution(i):
    primeString = makePrimeString(i + idDigitCount)

    return primeString[i:i + idDigitCount]

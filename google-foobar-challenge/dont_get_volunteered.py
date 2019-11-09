# Don't Get Volunteered!
# ======================
#
# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker.
# It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure
# that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the
# henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement
# puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead,
# you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test
# subject for the LAMBCHOP doomsday device!
#
# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in
# two parameters: the source square, on which you start, and the destination square, which is where you need to land
# to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take
# for you to travel from the source square to the destination square using a chess knight's moves (that is,
# two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa,
# in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive,
# and are numbered like the example chessboard below:
#
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution(0, 1)
# Output:
#     3
#
# Input:
# solution.solution(19, 36)
# Output:
#     1
#
# -- Java cases --
# Input:
# Solution.solution(19, 36)
# Output:
#     1
#
# Input:
# Solution.solution(0, 1)
# Output:
#     3
#
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit
# [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

cols = 8
rows = 8


def getRow(square):
    return square // cols


def getCol(square):
    return square % cols


def forceVerticalBoundaries(src, dest):
    startSquare = getCol(src)
    endSquare = startSquare + (rows - 1) * cols

    if dest < startSquare:
        return startSquare

    if dest > endSquare:
        return endSquare

    return dest


def forceHorizontalBoundaries(src, dest):
    srcRow = getRow(src)
    startSquare = srcRow * cols
    endSquare = startSquare + (cols - 1)

    if dest < startSquare:
        return startSquare

    if dest > endSquare:
        return endSquare

    return dest


def moveVertically(src, signedDy=1):
    return forceVerticalBoundaries(src, src + signedDy * cols)


def moveHorizontally(src, signedDx=1):
    return forceHorizontalBoundaries(src, src + signedDx)


def calculateSignedDx(src, dest):
    return getCol(dest) - getCol(src)


def calculateDx(src, dest):
    return abs(calculateSignedDx(src, dest))


def calculateHorizontalDirection(src, dest):
    return calculateSignedDx(src, dest) // calculateDx(src, dest)


def calculateSignedDy(src, dest):
    return getRow(dest) - getRow(src)


def calculateDy(src, dest):
    return abs(calculateSignedDy(src, dest))


def calculateVerticalDirection(src, dest):
    return calculateSignedDy(src, dest) // calculateDy(src, dest)


def shouldReroute(src, dx, dy, dest):
    newDx = calculateDx(src, dest)
    newDy = calculateDy(src, dest)

    return (
                   dx + dy < 3 and
                   (
                           (newDx + newDy <= dx + dy) or
                           (newDx + newDy == 3 and (newDx == 0 or newDy == 0)) or
                           (newDx + newDy > 3)
                   )
            ) or (3 < dx + dy < newDx + newDy) or (dx + dy == 4 and newDx + newDy != 3)  # special case


def canMoveHorizontally(src, signedDx):
    return getRow(src) == getRow(src + signedDx)


def canMoveVertically(src, signedDy):
    return 0 <= src + signedDy * cols < rows * cols


def solution(src, dest):
    moveCount = 0
    visitStates = [False] * (rows * cols)

    if src == dest:
        return moveCount

    dx = calculateDx(src, dest)
    dy = calculateDy(src, dest)

    currentSquare = src
    visitStates[currentSquare] = True
    failedOnce = False
    toggle = False

    while True:
        # corner case
        if dx == cols - 1 and dy == rows - 1:
            toggle = True

        if dx != 0 and dy != 0 and (dx + dy) % 3 == 0 and dx != dy:
            return moveCount + ((dx + dy) // 3)

        if dy < dx and not failedOnce:
            if dy == 0 and dx % 2 == 1 and dx != 3:
                hMove = calculateHorizontalDirection(currentSquare, dest) * 1
                vMove = 2
            else:
                hMove = calculateHorizontalDirection(currentSquare, dest) * min(dx, 2)
                vMove = 3 - min(dx, 2)

            if not canMoveVertically(currentSquare, vMove):
                vMove = -vMove

            newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            if shouldReroute(newSquare, dx, dy, dest) or visitStates[newSquare]:
                hMove = calculateHorizontalDirection(currentSquare, dest) * (3 - min(dx, 2))
                vMove = min(dx, 2)

                if not canMoveVertically(currentSquare, vMove):
                    vMove = -vMove

                newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)
                failedOnce = visitStates[newSquare]

        elif dx < dy and not failedOnce:
            if dx == 0 and dy % 2 == 1 and dy != 3:
                hMove = 2
                vMove = calculateVerticalDirection(currentSquare, dest) * 1
            else:
                hMove = 3 - min(dy, 2)
                vMove = calculateVerticalDirection(currentSquare, dest) * min(dy, 2)

            if not canMoveHorizontally(currentSquare, hMove):
                hMove = -hMove

            newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            if shouldReroute(newSquare, dx, dy, dest) or visitStates[newSquare]:
                hMove = min(dy, 2)
                vMove = calculateVerticalDirection(currentSquare, dest) * (3 - min(dy, 2))

                if not canMoveHorizontally(currentSquare, hMove):
                    hMove = -hMove

                newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)
                failedOnce = visitStates[newSquare]

        else:
            hMove = calculateHorizontalDirection(currentSquare, dest) * min(dx, 2)
            vMove = calculateVerticalDirection(currentSquare, dest) * (3 - min(dx, 2))

            if not canMoveHorizontally(currentSquare, hMove):
                hMove = -hMove

            if not canMoveVertically(currentSquare, vMove):
                vMove = -vMove

            newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            if shouldReroute(newSquare, dx, dy, dest) or visitStates[newSquare]:
                if abs(hMove) < abs(vMove):
                    if canMoveHorizontally(currentSquare, -hMove):
                        hMove = -hMove
                else:
                    if canMoveVertically(currentSquare, -vMove):
                        vMove = -vMove

                newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            if shouldReroute(newSquare, dx, dy, dest) or visitStates[newSquare]:
                hMove = calculateHorizontalDirection(currentSquare, dest) * (3 - min(dx, 2))
                vMove = calculateVerticalDirection(currentSquare, dest) * min(dx, 2)

                if not canMoveHorizontally(currentSquare, hMove):
                    hMove = -hMove

                if not canMoveVertically(currentSquare, vMove):
                    vMove = -vMove

                newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            if shouldReroute(newSquare, dx, dy, dest) or visitStates[newSquare]:
                if abs(hMove) < abs(vMove):
                    if canMoveHorizontally(currentSquare, -hMove):
                        hMove = -hMove
                else:
                    if canMoveVertically(currentSquare, -vMove):
                        vMove = -vMove

                newSquare = moveHorizontally(moveVertically(currentSquare, vMove), hMove)

            failedOnce = False

        if not failedOnce:
            moveCount += 1
            currentSquare = newSquare
            visitStates[currentSquare] = True

            dx = calculateDx(currentSquare, dest)
            dy = calculateDy(currentSquare, dest)

            if toggle:
                temp = currentSquare
                currentSquare = dest
                dest = temp

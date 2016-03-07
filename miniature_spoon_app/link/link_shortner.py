import math

BASE = 62

DIGIT_OFFSET = ord("0")
UPPERCASE_OFFSET = ord("A") - 10
LOWERCASE_OFFSET = ord("a") - 36

DIGIT_RANGE = 10
UPPERCASE_RANGE = 36
LOWERCASE_RANGE = 62


def numberConverter(i):
    assert isinstance(i, int)
    if 0 <= i < DIGIT_RANGE:
        return chr(i + DIGIT_OFFSET)
    elif DIGIT_RANGE <= i < UPPERCASE_RANGE:
        return chr(i + UPPERCASE_OFFSET)
    elif UPPERCASE_RANGE <= i < LOWERCASE_RANGE:
        return chr(i + LOWERCASE_OFFSET)
    else:
        raise ValueError(
            "%d is not a valid integer in the range of base %d" % i, BASE)


def characterConverter(c):
    assert isinstance(c, str)
    if c.isdigit():
        return ord(c) - DIGIT_OFFSET
    elif "A" <= c <= "Z":
        return ord(c) - UPPERCASE_OFFSET
    elif "a" <= c <= "z":
        return ord(c) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character of base  %d" % c, BASE)


def makeMiniature(giant):
    miniature = ""
    if giant == 0:
        miniature = "0"
    else:
        while giant > 0:
            piece = numberConverter(giant % BASE)
            miniature += piece
            giant /= BASE
    while len(miniature) < 6:
        miniature += "0"
    return miniature


def makeGiant(miniature):
    giant = 0
    for index, piece in enumerate(miniature):
        giant += characterConverter(piece) * int(math.pow(BASE, index))
    return giant

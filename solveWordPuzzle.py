import pprint
import pydash
import enchant
import sys

def solvePuzzle(string, numLetters=None, startsWith=None, contains=None):
    """
    1. Get the permutations of the string
    2. group them by the length of the string
    2.5 check them against an api to determine valid words
    3. pretty print
    """
    string = string.lower()
    if numLetters:
        numLettrs = int(numLetters)
    permutations = getPermutations(string)
    WordCheck = enchant.Dict("en_US")
    filtered = list(filter(lambda perm: len(perm) >= 3 and WordCheck.check(perm), permutations))
    permsByLen = pydash.collections.group_by(filtered, lambda x: len(x))
    if numLetters:
        permsByLen = permsByLen[numLetters]
        if startsWith:
            permsByLen = list(filter(lambda x: x[0] == startsWith, permsByLen))
        if contains:
            for char in contains:
                permsByLen = list(filter(lambda x: char in x, permsByLen))
    pprint.pprint(permsByLen)

def getPermutations(string):
    permutations = set()
    stringDict = {}
    for char in string:
        if char in stringDict:
            stringDict[char] += 1
        else:
            stringDict[char] = 0

    permutationHelper(string, "", permutations, stringDict)
    return permutations

def permutationHelper(string, perm, permutations, stringDict):
    if not string:
        return
    permutations.add(perm)
    permStringDict = {}
    for char in perm:
        if char in permStringDict:
            permStringDict[char] += 1
        else:
            permStringDict[char] = 0
    for index in range(len(string)):
        if string[index] in permStringDict and permStringDict[string[index]] + 1 > stringDict[string[index]]:
            continue
        perm += string[index]
        permutationHelper(string, perm, permutations, stringDict)
        perm = perm[0:len(perm) - 1]


if __name__== "__main__":
    while len(sys.argv) < 5:
        sys.argv.append("")
    solvePuzzle(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))


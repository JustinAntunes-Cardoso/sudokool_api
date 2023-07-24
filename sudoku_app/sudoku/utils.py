import math
import random

# Shuffles the numbers around in a row


def shuffle(lst):
    newList = lst
    for i in range(len(newList)):
        j = math.floor(random.random() * (i + 1))
        newList[i], newList[j] = newList[j], newList[i]

    return newList

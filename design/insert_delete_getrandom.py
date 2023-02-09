import random
from typing import List

# The essence of the task
TASK = """
All operations must be performed in O(1) time
"""


class RandomizedSet:

    def __init__(self):
        # numMap keys are added values, and numMap values are indexes of the same values stored in the numList
        # We can't just use a set (hashset), because the getrandom func would first need to convert it to a list in O(n) time
        self.numMap = {}         
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            # We add the new value as a key in the numMap, and append it to the numList, so it's index would equal
            # the length of the numList
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # To make this process in O(1) time, we look for the index of the value to be removed in the numMap, 
            # then overwrite this element in the numList with the last element of the numList,
            # and update corresponding indexes in the numMap
            idx = self.numMap[val]
            lastnum = self.numList[-1]
            self.numList[idx] = lastnum
            self.numList.pop()
            self.numMap[lastnum] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)

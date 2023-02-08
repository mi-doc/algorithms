import random
from typing import List

# The essence of the task
TASK = """
All operations must be performed in O(1) time
"""


class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastnum = self.numList[-1]
            self.numList[idx] = lastnum
            self.numList.pop()
            self.numMap[lastnum] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)
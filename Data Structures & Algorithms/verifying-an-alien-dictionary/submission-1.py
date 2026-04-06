from copy import copy
from functools import cmp_to_key
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c : i for i, c in enumerate(order)}

        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)
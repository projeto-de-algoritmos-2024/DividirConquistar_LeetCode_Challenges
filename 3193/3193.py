from itertools import permutations
from typing import List

class Solution:
    MOD = 10**9 + 7

    def countInversionsBruteForce(self, arr: List[int]) -> int:
        inversions = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        valid_count = 0

        for perm in permutations(range(n)):
            valid = True
            for endi, cnti in requirements:
                if self.countInversionsBruteForce(perm[:endi + 1]) != cnti:
                    valid = False
                    break
            if valid:
                valid_count += 1
                valid_count %= self.MOD

        return valid_count

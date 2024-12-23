from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(lo: int, hi: int) -> int:
            if lo == hi:
                return 0

            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)

            j = k = t = mid + 1
            temp = []
            for i in range(lo, mid + 1):
                while k <= hi and prefix_sums[k] - prefix_sums[i] < lower:
                    k += 1
                while j <= hi and prefix_sums[j] - prefix_sums[i] <= upper:
                    j += 1
                count += j - k

                while t <= hi and prefix_sums[t] < prefix_sums[i]:
                    temp.append(prefix_sums[t])
                    t += 1
                temp.append(prefix_sums[i])

            while t <= hi:
                temp.append(prefix_sums[t])
                t += 1

            prefix_sums[lo:hi + 1] = temp

            return count

        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        return merge_sort(0, len(prefix_sums) - 1)
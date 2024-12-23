from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start: int, end: int) -> int:
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            left, right = nums[start:mid+1], nums[mid+1:end+1]
            i, j = 0, 0
            merged = []
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            nums[start:end+1] = merged
            
            return count
        
        return merge_sort(0, len(nums) - 1)
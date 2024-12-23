class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        count = 0
        
        # Calcula todas as somas de subarrays
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                # Verifica se a soma está dentro do intervalo [lower, upper]
                if lower <= curr_sum <= upper:
                    count += 1
        
        return count

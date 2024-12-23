class Solution:
    def reversePairs(self, nums):
        # Função principal para contar os pares
        def mergeSort(nums, start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)  # Dividir e contar recursivamente
            count += merge(nums, start, mid, end)  # Contar inversões no merge
            return count
        
        # Função de merge que conta os pares
        def merge(nums, start, mid, end):
            count = 0
            left, right = start, mid + 1
            # Contando os pares de inversão durante o merge
            for i in range(start, mid + 1):
                while right <= end and nums[i] > 2 * nums[right]:
                    right += 1
                count += (right - (mid + 1))
            
            # Merge convencional
            temp = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if nums[left] < nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= end:
                temp.append(nums[right])
                right += 1
            
            for i in range(len(temp)):
                nums[start + i] = temp[i]
                
            return count

        return mergeSort(nums, 0, len(nums) - 1)

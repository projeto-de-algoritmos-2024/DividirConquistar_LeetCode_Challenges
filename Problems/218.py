from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # limites do eixo x
        min_x = min(building[0] for building in buildings)
        max_x = max(building[1] for building in buildings)
        
        # Armazena as alturas em cada ponto do eixo x
        heights = [0] * (max_x + 1)
        
        for left, right, height in buildings:
            for x in range(left, right):  
                heights[x] = max(heights[x], height)
        
        result = []
        prev_height = 0
        
        for x in range(len(heights)):
            current_height = heights[x]
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height
        
        if result and result[-1][1] != 0:
            result.append([max_x, 0])
        
        return result

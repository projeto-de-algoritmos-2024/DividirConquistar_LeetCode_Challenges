class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        # Divida os prédios em dois subconjuntos
        mid = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        
        # Mesclar os dois skylines
        return self.mergeSkylines(left_skyline, right_skyline)

    def mergeSkylines(self, left, right):
        h1 = h2 = 0 
        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            # Escolha o ponto com menor coordenada x
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else: 
                x, h1 = left[i]
                h2 = right[j][1]
                i += 1
                j += 1

            # A altura do contorno é o máximo entre h1 e h2
            max_height = max(h1, h2)
            if not merged or merged[-1][1] != max_height:
                merged.append([x, max_height])

        # Adicione os pontos restantes
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged

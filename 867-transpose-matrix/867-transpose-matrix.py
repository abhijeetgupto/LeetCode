class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix = list(map(list, zip(*matrix)))
        return t_matrix
        
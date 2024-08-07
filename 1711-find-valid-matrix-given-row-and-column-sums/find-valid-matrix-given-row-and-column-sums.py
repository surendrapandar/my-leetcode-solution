class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        COLS = len(colSum)
        output = [[0] * COLS for _ in range(len(rowSum))]

        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                minimum_val = min(rowSum[row], colSum[col])
                rowSum[row] -= minimum_val
                colSum[col] -= minimum_val                
                output[row][col] = minimum_val

        
        return output 
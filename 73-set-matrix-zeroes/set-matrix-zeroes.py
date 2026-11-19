class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        init_row_zero=False
        for i in matrix[0]:
            if i ==0:
                init_row_zero=True
        init_col_zero=False
        for j in range(len(matrix)):
            if matrix[j][0]==0:
                init_col_zero=True

        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    matrix[r][0]=0
        
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        if init_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i]=0
        if init_col_zero:
            for i in range(len(matrix)):
                matrix[i][0]=0
        
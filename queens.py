# Solver for N-Queens problem
# author - shubhamtibra

# Base class representing the problem
class Queens(object):

    def __init__(self, n):
        """
        Examles
        =======
        >>> Queens(4)
        0 [ 0 ,   0 ,   1 ,   0 ]
        1 [ 1 ,   0 ,   0 ,   0 ]
        2 [ 0 ,   0 ,   0 ,   1 ]
        3 [ 0 ,   1 ,   0 ,   0 ]
        """

        self.n = n
        self.ans = [[0 for i in range(self.n)] for j in range(self.n)]
        self.solve(0)
        printMatrix(self.ans)

    def __str__(self):
        return ''

    __repr__ = __str__

    def solve(self, col):
        """
        Solve the N-Queen problem
        """
        # if we pass the last column return True
        if col >= self.n:
            return True

        for i in range(self.n):

            if self._canplace(i, col):
                self.ans[i][col] = 1

                if self.solve(col+1):
                    return True
                else:
                    self.ans[i][col] = 0

        return False

    def _canplace(self, a, b):
        """
        Helper function to test if the position (a, b) is suitable.
        """
        for i in range(b):
            if self.ans[a][i]:
                return False

        i = a
        j = b
        while i >= 0 and j >= 0:

            if self.ans[i][j]:
                return False
            i=i-1; j=j-1

        i = a
        j = b
        while j >= 0 and i < self.n:
            if self.ans[i][j]:
                return False
            i = i+1
            j = j-1

        return True

def printMatrix(testMatrix):
        for i, element in enumerate(testMatrix):
              print (i, ' '.join(str(element)))

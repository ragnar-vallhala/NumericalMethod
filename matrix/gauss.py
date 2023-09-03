class Matrix:
    mat = []
    shape = (0,0)



    def __init__(self,mat) -> None:
        n = len(mat)

        if type(mat[0])!=list:
            raise "Cant create matrix!"
           

        k = len(mat[0])

        for i in mat:
            if len(i)!=k:
               raise "Cant create matrix!"
            self.mat.append(i)

        self.shape = (n,k)



    def __str__(self) -> str:
        res = "["

        for i in self.mat[:-1]:
            res+= str(i) + "\n"
        
        res+=str(self.mat[-1]) +"]"


        return res




    def isLowerTriangular(self) -> bool:

        for i in range(self.shape[0]):
            for k in range(i+1,self.shape[1]):
                if self.mat[i][k]!=0:
                    return False
        
        return True



    def isUpperTriangular(self) -> bool:

        for i in range(self.shape[0]):
            for k in range(0,i):
                if self.mat[i][k]!=0:
                    return False
        
        return True




    def solveUpperTriangular(self,d) -> list:
        ans = []
        if (not self.isUpperTriangular()) or self.shape[0]!=len(d):
            raise "Can't Solve"

        for i in range(self.shape[0]-1,-1,-1):
            sigma = 0
            for k in range(self.shape[0]-1,i,-1):
                sigma+= ans[k-self.shape[0]+1]*self.mat[i][k]
            
            ans.append((d[i]-sigma)/self.mat[i][i])
        ans.reverse()
        return ans




    def solveLowerTriangular(self,d) -> list:
        ans = []
        if (not self.isLowerTriangular()) or self.shape[0]!=len(d):
            raise "Can't Solve"

        for i in range(self.shape[0]):
            sigma = 0
            for k in range(0,i):
                sigma+= ans[k]*self.mat[i][k]
            
            ans.append((d[i]-sigma)/self.mat[i][i])
        return ans
               


def main():
    arr = [[1,0,0],[3,5,0],[2,3,1]]

    mat = Matrix(arr)

    print(mat.isLowerTriangular())
    print(mat.solveLowerTriangular([2,16,12]))

main()
        
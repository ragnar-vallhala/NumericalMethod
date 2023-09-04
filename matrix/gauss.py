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

    def __init__(self,shape,attribute):
        self.shape = shape
        if attribute=="Zeros":
            for i in range(shape[0]):
                self.mat.append([0]*shape[1])
        
        elif attribute=="Ones":
            for i in range(shape[0]):
                self.mat.append([1]*shape[1])

        elif attribute=="Identity":
            if self.shape[0]!=self.shape[1]:
                raise "Not a square matrix"
            
            for i in range(shape[0]):
                self.mat.append([0]*shape[1])

            for i in range(shape[0]):
                self.mat[i][i]=1
        else:
            raise "Invalid arg"



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

    

    def LUdecompose(self) -> tuple:
        """
        Not finished
        """
        L = Matrix(self.shape,"Zeros")
        U = Matrix(self.shape,"Identity")

        for i in range(self.shape[0]):
            L[i][1] = self.mat[i][1]

        for i in range(1,self.shape[0]):
            U[1][i] = self.mat[1][i]/L[1][1]
        
        for i in range(1,self.shape[0]-1):
            for j in range(i,self.shape[0]):
                L[i][j] = self.mat[i][j]
                for k in range(0,j):
                    L[i][j]-=L[i][k]*U[k][j]



def main():
    arr = [[1,0,0],[3,5,0],[2,3,1]]

    mat = Matrix((5,5),"Identity")
    print(mat)
    

main()
        
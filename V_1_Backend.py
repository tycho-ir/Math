import numpy as np

def Sigma(i, j):
    for k in range(0, 2):
        for x in range(i, j):
            b.append(x)
        j = i
        i = 0
        if sum(b)== 0 :
            SUMB=1
        else :
            SUMB = sum(b)
        C.append(SUMB)
        b.clear()
    return(C)
i=0
x=[1]
b=[]
C=[]
A=np.array([ [16,3],[7,11] ])
l=len(A)
B=np.array([11,13])
J=Sigma(i,l)
x.append(1/A[i,i]*( B[i]- (A[i,J[0]]) ) )
print(x)

from appJar import gui
import numpy as np
app=gui("UI","700x250"
        )

i = 0
x = [1]
b = []
C = []
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

def Get(Get):

    A = np.array([[app.getEntry("x1"), app.getEntry("x2")],
                  [app.getEntry("x1 2"), app.getEntry("x2 2")]
                  ])
    l = len(A)
    B=np.array([app.getEntry("Result") ,app.getEntry("Result 2")])
    J = Sigma(i, l)
    x.append(1 / A[i, i] * (B[i] - (A[i, J[0]])))
    print(x)






app.setBg("white")
app.addNumericEntry("x1",1,0)
app.addLabel("X(1)","x(1)",1,1)
app.addNumericEntry("x2",1,2)
app.addLabel("X(2)","x(2)",1,3)
app.addLabel("=(1)","=",1,4)
app.addNumericEntry("Result",1,5)

app.addNumericEntry("x1 2",2,0)
app.addLabel("X(1)_2","x(1)",2,1)
app.addNumericEntry("x2 2",2,2)
app.addLabel("X(2)_2","x(2)",2,3)
app.addLabel("=(1)_2","=",2,4)
app.addNumericEntry("Result 2",2,5)



app.addButton("Get",Get,4,2)
app.go()

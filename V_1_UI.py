from appJar import gui


app=gui("UI","700x250")

def Get(Get):
    pass




app.setBg("white")
app.addNumericEntry("x1",1,0)
app.addLabel("X(1)","x(1)",1,1)
app.addNumericEntry("x2",1,2)
app.addLabel("X(2)","x(2)",1,3)
app.addLabel("=(1)","=",1,4)
app.addNumericEntry("Result",1,5)

app.addNumericEntry("x1_2",2,0)
app.addLabel("X(1)_2","x(1)",2,1)
app.addNumericEntry("x2_2",2,2)
app.addLabel("X(2)_2","x(2)",2,3)
app.addLabel("=(1)_2","=",2,4)
app.addNumericEntry("Result_2",2,5)



app.addButton("Get",Get,4,2)
app.go()
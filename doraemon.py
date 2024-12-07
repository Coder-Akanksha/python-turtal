from turtle import*

def my_goto(x,y):
    penup()
    goto(x,y)
    pendown()
def eyes():
    fillcolor("#ffffff")
    begin_fill()
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0<= i < 30 or 60 <=i <90:
            a -=0.05
            lt(3)
            fd(a)
        else:
            a+=0.05
            lt(3)
            fd(a)
            tracer(True)
            end_fill()
def beard():
    my_goto(-32,135)
    seth(165)
    fd(60)
    my_goto(-32,125)
    seth(180)
    fd(60)
    my_goto(37,135)
    seth(15)
    fd(60)
    my_goto(37,125)
    seth(0)
    fd(60)
    my_goto(37,115)
    seth(-13)
    fd(60)
    

def mouth():
    my_goto(5,148)
    seth(270)
    fd(100)
    seth(0)
    circle(120,50)
    seth(230)
    circle(-120,100)

def scarf():
    fillcolor("#e70010")
    begin_fill()
    seth(0)
    fd(200)
    circle(-5,90)
    fd(10)
    circle(-5,90)
    fd(207)
    circle(-5,90)
    fd(10)
    circle(-5,90)
    end_fill()
def nose():
    my_goto(-10,158)
    seth(315)
    fillcolor("#e70010")
    begin_fill
def black_eyes():
    pass
def face():
    pass
def head():
    pass
def Doraemon():
    pass

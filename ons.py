import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light yellow")
skk = turtle.Turtle()
skk.color("red")


def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(200)
        size = size + 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)



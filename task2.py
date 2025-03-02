import turtle

def treeFractal(TTL, recursionLevel, branchLength, branchReduction=None, angle=45):
    """Малювання дерева Піфагора"""
    if branchReduction is None:
        branchReduction = branchLength//(recursionLevel + 1)

    if recursionLevel == 0:
        TTL.fd(0)
    else:
        branchLength = branchLength - branchReduction
        TTL.forward(branchLength)
        TTL.left(angle)
        treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
        TTL.right(angle * 2)
        treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
        TTL.left(angle)
        TTL.backward(branchLength)


try:
    recursionLevel = int(input("Введіть рівень рекурсії: "))
    if recursionLevel > 0:
        screen = turtle.Screen() 
        screen.setup(600, 600)  

        TTL = turtle.Turtle()
        TTL.speed(0) 
        TTL.color("red")
        TTL.pensize(2) 

        TTL.penup() 
        TTL.setposition(0, -100)
        TTL.pendown() 
        TTL.hideturtle()
        TTL.setheading(90)
        treeFractal(TTL, 8, 80)

        screen.exitonclick()

    else:
        print("Рівень рекурсії не може бути відʼємним числом.")

except ValueError:
    print("Введено не ціле число. Запусіть програму ще раз та введіть коректне значення.")
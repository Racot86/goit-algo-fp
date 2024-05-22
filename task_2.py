"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

"""
import turtle
import math

def draw_tree(t, branch_length, angle, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    current_pos = t.position()
    current_heading = t.heading()
    
    t.right(angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    
    t.setposition(current_pos)
    t.setheading(current_heading)
    
    t.left(angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    
    t.setposition(current_pos)
    t.setheading(current_heading)
    
def main():
    level = int(input("Enter recursion level: "))
    
    
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.color("brown")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)
    
    
    draw_tree(t, 100, 45, level)
    
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

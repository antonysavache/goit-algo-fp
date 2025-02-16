
import turtle
import math

def draw_pythagoras_tree(t, size, level):
    if level == 0:
        return

    # Draw the base square
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)

    # Save the current position and heading
    save_pos = t.position()
    save_heading = t.heading()

    # Move to the position for right branch
    t.forward(size)
    t.left(45)

    # Calculate size of branches using Pythagorean theorem
    branch_size = size / math.sqrt(2)

    # Recursively draw right branch
    draw_pythagoras_tree(t, branch_size, level - 1)

    # Return to saved position and heading
    t.penup()
    t.goto(save_pos)
    t.setheading(save_heading)
    t.pendown()

    # Move to position for left branch
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(45)

    # Recursively draw left branch
    draw_pythagoras_tree(t, branch_size, level - 1)

    # Return to saved position and heading
    t.penup()
    t.goto(save_pos)
    t.setheading(save_heading)
    t.pendown()

def setup_turtle():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.color("green")
    t.left(90)  # Point upward

    # Move to starting position
    t.penup()
    t.goto(0, -200)  # Start from bottom of screen
    t.pendown()

    return t, screen

def main():
    # Get recursion level from user
    level = int(input("Enter the recursion level (1-10): "))
    level = max(1, min(10, level))  # Limit level between 1 and 10

    # Setup turtle
    t, screen = setup_turtle()

    # Draw the tree
    draw_pythagoras_tree(t, 100, level)  # 100 is the size of the base square

    # Hide turtle and keep window open
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
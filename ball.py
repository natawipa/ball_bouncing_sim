import turtle
import random

'''
def draw_circle(color, size, x, y):
    # draw a circle of radius equals to size at x, y coordinates and paint it with color
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
    xpos[i] += vx[i]
    ypos[i] += vy[i]

    # if the ball hits the side walls, reverse the vx velocity
    if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    # if the ball hits the ceiling or the floor, reverse the vy velocity
    if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]

def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    for i in range(num_balls):
        xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01*canvas_width))
        vy.append(random.randint(1, 0.01*canvas_height))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
'''

# class Ball:
#     def __init__(self, speed, size, canvas_width, canvas_height):
#         self.location = self.initial_position(canvas_width, canvas_height)
#         self.speed = speed
#         self.color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#         self.size = size
#
#     def initial_position(self, canvas_width, canvas_height):
#         x = random.randint(0, canvas_width)
#         y = random.randint(0, canvas_height)
#         return (x, y)
#
#     def move(self):
#         self.xpos += self.vx
#         self.ypos += self.vy

class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        # Initialize the ball with random position, velocity, color, and radius
        self.x = random.randint(-1 * canvas_width + ball_radius, canvas_width - ball_radius)
        self.y = random.randint(-1 * canvas_height + ball_radius, canvas_height - ball_radius)
        self.vx = random.uniform(1, 0.01 * canvas_width)
        self.vy = random.uniform(1, 0.01 * canvas_height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = ball_radius

    def draw_circle(self):
        # Draw the ball on the turtle canvas
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def move_circle(self, canvas_width, canvas_height):
        # Move the ball and handle collisions with walls
        self.x += self.vx
        self.y += self.vy

        if abs(self.x + self.vx) > (canvas_width - self.radius):
            self.vx = -self.vx

        if abs(self.y + self.vy) > (canvas_height - self.radius):
            self.vy = -self.vy

def initilizing(canvas_width, canvas_height, ball_radius, num_balls):
    # Create a list of Ball objects with random properties
    return [Ball(canvas_width, canvas_height, ball_radius) for _ in range(num_balls)]

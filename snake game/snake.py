from turtle import Turtle

# defining some constants 
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.snake_head = self.segments[0]

    def create_snake_body(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move_snake(self):
        for segment_number in range(len(self.segments)-1,0,-1):
            # here we need to make every segment move to the location of its previous segment 
            new_position = self.segments[segment_number - 1].pos()
            # print(new_position)
            self.segments[segment_number].goto(new_position)
        
        # after this loop we need to move the first piece one step and the loop will make the left pieces do that
        self.snake_head.forward(20)

    def move_up(self):
        if self.snake_head.heading() != SOUTH:
            self.snake_head.setheading(NORTH)

    def move_down(self):
        if self.snake_head.heading() != NORTH:
            self.snake_head.setheading(SOUTH)
        
    def move_right(self):
        if self.snake_head.heading() != WEST:
            self.snake_head.setheading(EAST)

    def move_left(self):
        if self.snake_head.heading() != EAST:
            self.snake_head.setheading(WEST)
from random import randint

from direction import Direction
from position import Position

INITIAL_SNAKE = [
    Position(1, 2),
    Position(2, 2),
    Position(3, 2)
]
INITIAL_DIRECTION = Direction.RIGHT


class GameState:
    def __init__(self,
                 snake=None,
                 direction=INITIAL_DIRECTION,
                 food=None,
                 field_size=20):
        self.field_size = field_size
        self.direction = direction

        if snake is None:
            snake = INITIAL_SNAKE
        self.snake = snake

        if food is None:
            self.set_random_food_position()
        self.food = food


    def next_head(self, direction):
        pos = self.snake[-1]
        match direction:
            case Direction.UP:
                return Position(pos.x, (pos.y - 1) % self.field_size)
            case Direction.DOWN:
                return Position(pos.x, (pos.y + 1) % self.field_size)
            case Direction.RIGHT:
                return Position((pos.x + 1) % self.field_size, pos.y)
            case Direction.LEFT:
                return Position((pos.x - 1) % self.field_size, pos.y)

    def set_random_food_position(self):
        self.food = Position(
            randint(0, self.field_size - 1),
            randint(0, self.field_size - 1)
        )

        if self.food in self.snake:
            self.set_random_food_position()

    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    def can_turn(self, direction):
        new_head = self.next_head(direction)
        return new_head != self.snake[-2]

    def step(self):
        new_head = self.next_head(self.direction)

        collision = new_head in self.snake
        if collision:
            self.set_initial_position()
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]

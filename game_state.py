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
                 snake,
                 direction,
                 food,
                 field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

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


    def step(self):
        new_head = self.next_head(self.direction)

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]

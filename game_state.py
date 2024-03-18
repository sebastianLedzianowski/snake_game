from direction import Direction
from position import Position

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
                return Position(pos.x,
                                (pos.y - 1) % self.field_size)
            case Direction.DOWN:
                return Position(pos.x,
                                (pos.y + 1) % self.field_size)
            case Direction.RIGHT:
                return Position((pos.x + 1) % self.field_size,
                                pos.y)
            case Direction.LEFT:
                return Position((pos.x - 1) % self.field_size,
                                pos.y)

    def step(self):
        new_head = self.next_head(self.direction)
        self.snake.append(new_head)
        self.snake = self.snake[1:]

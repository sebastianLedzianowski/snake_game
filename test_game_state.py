import unittest

from game_state import GameState
from position import Position
from direction import Direction


class GameStateTest(unittest.TestCase):

    def test_snake_should_move_right(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20,
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(2, 4)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_left(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.LEFT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(0, 4)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_up(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(2, 2),
                Position(3, 2)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 2),
            Position(3, 2),
            Position(3, 1)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_down(self):
        state = GameState(
            snake=[
                Position(2, 2),
                Position(3, 2),
                Position(4, 2)
            ],
            direction=Direction.DOWN,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(3, 2),
            Position(4, 2),
            Position(4, 3)
        ]
        self.assertEqual(expected_state, state.snake)


    def test_snake_should_move_up_on_top(self):
        state = GameState(
            snake=[
                Position(2, 2),
                Position(2, 1),
                Position(2, 0)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 1),
            Position(2, 0),
            Position(2, 19)
        ]
        self.assertEqual(expected_state, state.snake)


    def test_snake_should_move_right_on_edge(self):
        state = GameState(
            snake=[
                Position(17, 1),
                Position(18, 1),
                Position(19, 1)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(18, 1),
            Position(19, 1),
            Position(0, 1)
        ]
        self.assertEqual(expected_state, state.snake)


    def test_snake_should_move_left_on_edge(self):
        state = GameState(
            snake=[
                Position(2, 1),
                Position(1, 1),
                Position(0, 1)
            ],
            direction=Direction.LEFT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 1),
            Position(0, 1),
            Position(19, 1)
        ]
        self.assertEqual(expected_state, state.snake)


    def test_snake_should_move_down_on_edge(self):
        state = GameState(
            snake=[
                Position(2, 17),
                Position(2, 18),
                Position(2, 19)
            ],
            direction=Direction.DOWN,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 18),
            Position(2, 19),
            Position(2, 0)
        ]
        self.assertEqual(expected_state, state.snake)
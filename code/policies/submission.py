import numpy as np
import random

class HeuristicGomokuAI:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size

    def evaluate_board(self, board, player_index):
        score = 0
        for x in range(self.board_size):
            for y in range(self.board_size):
                if board[player_index, x, y] == 1:
                    score += self.evaluate_position(board, x, y, player_index)
        return score

    def evaluate_position(self, board, x, y, player_index):
        position_score = 0
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            line_length, open_ends, blocked_ends, four_in_a_row, three_in_a_row = self.check_line(board, x, y, dx, dy, player_index)
            # existing scoring logic...
            position_score += four_in_a_row * 500  # new scoring for four-in-a-row
            position_score += three_in_a_row * 300  # new scoring for three-in-a-row
        return position_score

    def get_possible_moves(self, board):
        possible_moves = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                if board[0, x, y] == 0 and board[1, x, y] == 0:  # assuming 0 represents an empty position
                    possible_moves.append((x, y))
        return possible_moves

    def select_random_move(self, board):
        possible_moves = self.get_possible_moves(board)
        return random.choice(possible_moves) if possible_moves else None

class Submission:
    def __init__(self, board_size, win_size):
        self.heuristic_ai = HeuristicGomokuAI(board_size, win_size)

    def __call__(self, state):
        current_player = state.current_player()  # Determine the current player from the state
        valid_moves = state.valid_actions()  # Get valid moves
        return self.heuristic_ai.select_random_move(state.board, current_player, self.heuristic_ai.get_possible_moves(state.board))


# Assuming that the `state` object has a `current_player()` method and a `board` attribute

# Example usage
if __name__ == "__main__":
    board_size = 15
    win_size = 5
    ai = HeuristicGomokuAI(board_size, win_size)
    board = np.zeros((board_size, board_size), dtype=int)  # 0 for empty, 1 for player 1, 2 for player 2
    current_player = 1

    while True:  # Add your own game-over condition check
        move = ai(board, current_player)
        board[move] = current_player
        current_player = 3 - current_player  # Switch player
        # Add display or logging of the board state

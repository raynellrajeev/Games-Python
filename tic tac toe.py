import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.winner = None
        self.current_player = "X"
        self.game_running = True
        
    def display_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
    
    def player_move(self):
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                if 0 <= position <= 8 and self.board[position] == " ":
                    self.board[position] = self.current_player
                    break
                else:
                    print("Invalid position! Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9!")
    
    def computer_move(self):
        empty_positions = [i for i, spot in enumerate(self.board) if spot == " "]
        if empty_positions:
            position = random.choice(empty_positions)
            self.board[position] = self.current_player
    
    def check_winner(self):
        # Check winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != " "):
                self.winner = self.board[combo[0]]
                return True
        return False
    
    def check_tie(self):
        return " " not in self.board
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def play_again(self):
        while True:
            choice = input("Play again? (y/n): ").lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            print("Please enter 'y' or 'n'")
    
    def play_game(self):
        print("\nWelcome to Tic Tac Toe!")
        while True:
            try:
                mode = int(input("1. Play with a friend\n2. Play with computer\nSelect mode: "))
                if mode in [1, 2]:
                    break
                print("Please enter 1 or 2!")
            except ValueError:
                print("Please enter a valid number!")
        
        while self.game_running:
            self.display_board()
            
            if mode == 1 or (mode == 2 and self.current_player == "X"):
                self.player_move()
            else:
                self.computer_move()
            
            if self.check_winner():
                self.display_board()
                print(f"\nPlayer {self.winner} wins!")
                if not self.play_again():
                    break
                self.__init__()  # Reset the game
                continue
            
            if self.check_tie():
                self.display_board()
                print("\nIt's a tie!")
                if not self.play_again():
                    break
                self.__init__()  # Reset the game
                continue
            
            self.switch_player()
        
        print("Thanks for playing!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

import random

VALID_INPUTS = {'head', 'tail'}
MAX_RUNS = 6
TOSS_ROUNDS = 3
TOSS_WINS_NEEDED = 2

class CricketGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def get_valid_number(self, prompt: str) -> int:
        """Get valid number input between 0 and MAX_RUNS."""
        while True:
            try:
                num = int(input(prompt))
                if 0 <= num <= MAX_RUNS:
                    return num
                print(f"Please enter a number between 0 and {MAX_RUNS}")
            except ValueError:
                print("Please enter a valid number")

    def toss(self) -> bool:
        """Handle the toss with input validation."""
        print("\n--------TOSS--------")
        print("Best out of three")
        wins = 0

        for _ in range(TOSS_ROUNDS):
            while True:
                choice = input("Head or Tail? :").lower()
                if choice in VALID_INPUTS:
                    break
                print("Please enter either 'head' or 'tail'")

            result = random.choice(list(VALID_INPUTS))
            print("Coin:", result)
            if choice == result:
                wins += 1

        return wins >= TOSS_WINS_NEEDED

    def play_innings(self, is_batting: bool) -> int:
        """Handle both batting and bowling innings."""
        print(f"\n--------{'BATTING' if is_batting else 'BOWLING'}--------")
        score = 0

        while True:
            player_num = self.get_valid_number(f"Enter number between 0 and {MAX_RUNS}: ")
            comp_num = random.randint(0, MAX_RUNS)
            print("Computer:", comp_num)

            if player_num == comp_num:
                print("OUT!")
                print("Score is", score)
                return score

            if is_batting:
                score += player_num
            else:
                score += comp_num
            print(f"Current score: {score}")

    def play_match(self, player_bats_first: bool):
        """Play a complete match."""
        first_innings = self.play_innings(player_bats_first)
        second_innings = self.play_innings(not player_bats_first)

        if player_bats_first:
            self.player_score, self.computer_score = first_innings, second_innings
        else:
            self.computer_score, self.player_score = first_innings, second_innings

    def play(self):
        """Main game loop."""
        while True:
            if self.toss():
                print("Toss won!")
                while True:
                    choice = input("batting or bowling? :").lower()
                    if choice in {'batting', 'bowling'}:
                        break
                    print("Please enter either 'batting' or 'bowling'")
                
                self.play_match(choice == 'batting')
            else:
                print("Toss lost, computer chose to bat.")
                self.play_match(False)

            # Determine winner
            if self.player_score > self.computer_score:
                print("Player wins!")
            else:
                print("Computer wins!")

            # Ask to play again
            while True:
                play_again = input("start or quit? ").lower()
                if play_again in {'start', 'quit'}:
                    break
                print("Please enter either 'start' or 'quit'")

            if play_again == 'quit':
                print("--------Thank you for playing--------")
                break
            print("--------New game-------")

if __name__ == "__main__":
    game = CricketGame()
    game.play()
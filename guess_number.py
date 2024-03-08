import sys
import random

# we have this parent function because we're going to need a closure to keep track of game count and player wins
def guess_number(name='PlayerOne'): 
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name # nonlocalize parent function's parameter
        nonlocal player_wins # game_count is not needed in this function

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number
            # recursion to relaunch play_guess_number

        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}.")
        print(
            f"I was thinking about the number {computerchoice}.\n"
        )

        player = int(playerchoice)
        computer = int(computerchoice) # now an integer number

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time."

            game_result = decide_winner(player, computer)
            print(game_result)

            nonlocal game_count
            game_count += 1

            print(f"\nGame count: {game_count}")
            print(f"\n{name}'s wins: {player_wins}")
            print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

            print(f"\nPlay again, {name}?")

            while True:
                playagain = input("\nY for Yes or \nQ to Quit\n")
                if playagain.lower() not in ["y", "q"]:
                    continue
                else:
                    break
            if playagain.lower() == "y":
                return play_guess_number()
            else:
                print("\nThank you for playing!\n")
                if __name__ == "__main__":
                    sys.exit(f"Bye, {name}!")
                else:
                    return # if launched from the arcade.py launcher, 
                    # this empty return exits function and takes you back to the arcade.py parent function
            
    return play_guess_number # closure, check that indent lines up with parent function

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name) # the guess_number function that receives the name from the user's arguments
    guess_my_number()





import random

import ascii_art as art

GAME_MOVES = [art.rock, art.paper, art.scissors]


def rock_paper_scissors() -> None:
    """Play Rock Paper Scissors against the computer."""
    random.seed()
    print("Welcome to Rock Paper Scissors!")

    player_move = input(
        "Which move are you going to make?\n"
        "Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
    )

    while player_move not in ["0", "1", "2"]:
        player_move = input(
            "That move is invalid. Let's try again.\n"
            "Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
        )

    player = GAME_MOVES[int(player_move)]
    computer = random.choice(GAME_MOVES)

    print(f"Your move: {player}")
    print(f"Computer's move: {computer}")

    if player == computer:
        print("Draw!")
    elif (
        (player == art.rock and computer == art.scissors)
        or (player == art.paper and computer == art.rock)
        or (player == art.scissors and computer == art.paper)
    ):
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    rock_paper_scissors()

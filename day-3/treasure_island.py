import ascii_art as art


def treasure_island() -> None:
    """Play Treasure Island, a Choose Your Own Adventure game."""
    print(art.island)
    print("Welcome to Treasure Island! Can you find the hidden treasure?")

    print(
        "\nYour boat lands on the rocky shore of a secluded desert island.\n"
        "After disembarking, you see a path that leads into the jungle.\n"
        "You continue down the path until you reach a crossroads."
    )
    direction = input(
        "Which direction do you want to go next? Left or right?\n"
    ).lower()

    if direction == "left":
        print(
            "\nAfter a brisk, invigorating hike, you come to a large lake with "
            "an island\nin the distance.\n"
            "An island within an island?\n"
            "You also see a tiny speck in the water that looks like a boat headed "
            "your way.\n"
            "Is the captain friendly? Or is it a group of pirates?\n"
            "You can wait to find out or you can try your luck swimming to the "
            "island."
        )
        lake = input("What do you want to do? Wait or swim?\n").lower()

        if lake == "wait":
            print(
                "\nThe gamble paid off.\n"
                "The boat belongs to a local guide, and after giving him your "
                "watch, he takes\nyou to the island.\n"
                'He says in perfect English, "Continue down the path to find '
                'the hidden treasure."\n'
                "Weird.\n"
                "Almost immediately, you come across an archaic stone structure "
                "that gives off\nsuper creepy vibes. This must be it.\n"
                "Upon entering the ruins, you are presented with three doors."
            )
            door = input(
                "Which door are you going through? Red, blue, or yellow?\n"
            ).lower()

            if door == "yellow":
                print(art.treasure)
                print(
                    "Congratulations!\n"
                    "You found the treasure!\n"
                    "Now you just have to figure out how you're going to get "
                    "it off the island."
                )
            elif door == "red":
                print(art.arrow)
                print("Ouch, you took an arrow straight to the face.\nGame over.")
            elif door == "blue":
                print(art.death)
                print(
                    "As the door locks behind you and water starts to pour into "
                    "the sealed room, you\nregret telling your spouse that you "
                    "were just going to Vegas with your friends.\n"
                    "Game over."
                )
            else:
                print(art.driven_mad)
                print(
                    "Oh no, you must have been driven mad by the curse of the "
                    "temple.\n"
                    "Did they not warn you about that?\n"
                    "Game over."
                )

        elif lake == "swim":
            print(art.crocodile)
            print(
                "The lake is saturated with crocodiles and bull sharks.\n"
                "You didn't even make it halfway across before becoming lunch.\n"
                "Game over."
            )
        else:
            print(art.necromancers)
            print(
                "Unfortunately, that caught the attention of a tribe of cannibal "
                "necromancers.\n"
                "Game over."
            )

    elif direction == "right":
        print(art.panther_king)
        print(
            "Oh no, that path led you directly to the realm of the Black Panther "
            "King, and he\nlikes exotic food.\n"
            "Game over."
        )
    else:
        print(art.maneaters)
        print(
            "You decide to forge your own path.\n"
            "You stumble into a grove of Man-Eaters.\n"
            "What a terrible decision.\n"
            "Game over."
        )


if __name__ == "__main__":
    treasure_island()

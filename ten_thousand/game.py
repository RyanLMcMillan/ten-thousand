from game_logic import GameLogic

def game_round(game_tracker):
    banker = game_tracker.get_banker()

    print(f"starting round {game_tracker.get_round()}")
    print(f"Rolling {game_tracker.get_die_count()} dice...")
    #test = [2, 1, 2, 2, 2, 4]
    roll = GameLogic.roll_dice(game_tracker.get_die_count())
    print(f"*** {tuple(roll)} ***")
    print("Enter dice to keep or (q)uit")
    cont = input("> ")
    if cont == "q":
        banker.commit_round_score()
        print(f"Thanks for playing. You earned {banker.get_score()} points.")
        game_tracker.quit()
        return

    die_count = game_tracker.get_die_count() - len(cont)
    game_tracker.set_die(die_count)
    round_score = GameLogic.calculate_score(tuple(cont))

    if round_score == 0:
        banker.abort_round_score()

    print(f"You have {round_score} unbanked points and {die_count} dice remaining")

    print("(r)oll again, (b)ank your points or (q)uit:")
    action = input("> ")
    if action == "q":
        print(f"Thanks for playing. You earned {banker.get_score()} points.")
        game_tracker.quit()
        return
    elif action == "r":
        game_round(game_tracker)
        pass
    elif action == "b":
        banker.add_score(round_score)
        pass

    banker.commit_round_score()


def play_game():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    start = input("> ")

    if start == "n":
        print("OK. Maybe another time")
        return

    game_tracker = GameTracker()

    game_round(game_tracker)

    while game_tracker.continue_playing():
        game_tracker.add_round()
        game_round(game_tracker)

        if game_tracker.get_round() == 20:
            print(f"Thank you for playing; you earned {game_tracker.get_score()} points.")
            pass
        pass


if __name__ == "__main__":
    play_game()
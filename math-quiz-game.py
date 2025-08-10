import random

INCORRECT = "Incorrect"
QUESTIONS = 10
TRIES = 3


def main():

    # intialize score
    score = 0

    # prompt the user to pick level 1, 2, or 3
    level = get_level()

    # prompt an equation n times to the user
    for _ in range(QUESTIONS):
        score += prompt_question(level)

    # print the score after game is over at n questions
    print_score(score)

# prompt the user for a valid level and return to main


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level


# generates random math question based on passed level. Returns 1 or 0 to add to score


def prompt_question(level):

    # generates math question and finds the answer
    x, y = generate_integer(level), generate_integer(level)
    current_answer = (x + y)

    # give the user n tries to answer each question correctly
    for attempt in range(TRIES):
        try:
            if int(input(f"{x} + {y} = ")) == current_answer:
                return 1
            else:
                print(INCORRECT)
                if attempt == TRIES - 1:

                    # prints the answer after n failed attempts and moves on
                    print(f"{x} + {y} = {current_answer}")
        except ValueError:
            print(INCORRECT)
    return 0

# returns an integer based on the user's selected level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def print_score(score):
    print(f"Score: {score}")

if __name__ == "__main__":
    main()

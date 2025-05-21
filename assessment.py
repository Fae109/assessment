# basic math
import random
import math



def string_checker(question, valid_ans=("yes", "no")):
    error = f"pls enter a valid option from the following list: {valid_ans}"

    while True:

        #
        user_responce = input(question).lower()

        for item in valid_ans:
            # check if user responce is a word in list
            if item == user_responce:
                return item

            # check if the user responce is the same as
            # the first letter of an item in the list
            elif user_responce == item[0]:
                return item

        #
        print(error)
        print()


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***
enter 000 to exit

    """)


def int_check(question):
    """checks user enters an int more than or equal to 1"""

    # int checker, to make sure user is using numbers
    while True:
        error = "pls enter an integer more then or equal to 1"

        to_check = input(question)

        #
        if to_check == "":
            return "infinite"
        elif to_check == "":
            return error
        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)



game_history = []

# main routine
print("enter 000 to exit")

# ask viewer if they want (cheek they say yes / no)
want_instructions = string_checker("do you want to see the instructions?")

# display the instructions wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")

# number list for questions
math_num_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
math_num_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# initialise game
mode = "regular"
rounds_played = 0
correct = 0
incorrect = 0



num_rounds = int_check("how many rounds would you like? push <enter> of infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    error = "pls enter an integer more then or equal to 1"

    try:
        # round heading
        if mode == "infinite":
            round_heading = f"\n♾️♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ️♾️♾️♾️♾️"
        else:
            round_heading = f"\n 💿💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿💿"

        # generate question
        print(round_heading)
        print()
        random_num1 = random.choice(math_num_list1)
        random_num2 = random.choice(math_num_list2)
        answer = random_num2 + random_num1
        user_answer = int_check(f"{random_num1} + {random_num2} = ")


        if user_answer == answer:
            feedback = ("correct")
            rounds_played += 1
            correct += 1

        elif user_answer == 000:
            print("over")
            end_game = "yes"
            break

        else:
            feedback = (f"incorrect: answer is {answer}")
            rounds_played += 1
            incorrect += 1

        round_feedback = (f"you are {feedback}")
        print(round_feedback)

    # if
        if mode == "infinite":
           num_rounds += 1

    except ValueError:
        print(error)




# end loop
if rounds_played == num_rounds:
    end_game = "yes"

# game stats
if end_game == "yes":
    print()
    print("📊📊📊📊 Game Stats 📊📊📊📊")
    print()
    print(f"you got {correct} out of {rounds_played} correct")
    print(f"you got {incorrect} out of {rounds_played} incorrect")

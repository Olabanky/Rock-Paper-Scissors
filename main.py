import random


def user_option(user):
    if user == "R":
        return "Rock"
    elif user == "P":
        return "Paper"
    elif user == "S":
        return "Scissors"


def computer_option(option):
    if option == "R":
        return "Rock"
    elif option == "P":
        return "Paper"
    elif option == "S":
        return "Scissors"


outcome = {
    "Rock": {"Rock": "It's a tie", "Paper": "computer won", "Scissors": "You won "},
    "Paper": {"Rock": "You won", "Paper": "It's a tie", "Scissors": "computer won"},
    "Scissors": {"Rock": "computer won", "Paper": "You won", "Scissors": "It's a tie"}
}

print(">>>>>>Welcome to the Rock-Paper-Scissors Game<<<<<<\n")

player_name = input("Please enter your name to proceed \n>>> ")

player_name = player_name.title()
welcome_message = (
    "Hello %s, please take note of the rules of the game: \n" % player_name)
print(welcome_message,
      "\n Rock beats Scissors \n Paper beats Rock \n Scissors beats Paper \n")

computer_score = 0
player_score = 0
rounds = 0

game_start = False

while not game_start:
    ready = int(input("Press 1 to start the game or press 2 to exit \n>>> "))
    if ready == 1:
        print('Rock! Paper! Scissors!')

        while rounds < 3:
            option = ["R", "P", "S"]
            computer_pick = random.choice(option)
            computer = computer_option(computer_pick)

            select_option = input(
                str("%s, please input R for Rock, P for Paper or S for Scissors \n>>> " % player_name)).upper()

            user_option(select_option)
            if (select_option == "R" and computer_pick == "S") or (select_option == "S" and computer_pick == "P") or (select_option == "P" and computer_pick == "R"):

                player_score += 1
                rounds += 1
            elif (computer_pick == "R" and select_option == "S") or (computer_pick == "S" and select_option == "P") or (computer_pick == "P" and select_option == "R"):

                computer_score += 1
                rounds += 1
            try:
                print("You selected : %s (%s) " % (select_option,
                      (user_option(select_option))))
                print("computer selected : %s (%s) " %
                      (computer_pick, computer))
                print("\n***Game outcome***")
                print(outcome[user_option(select_option)][computer])
                print(" _________________________\n"
                      "  %s  (%d) : computer (%d)"
                      "\n|_________________________|\n" % (player_name, player_score, computer_score))

            except:
                print("invalid input")

    elif ready == 2:
        game_start = False
        exit()
    else:
        print("you have entered an invailid option")
    if rounds == 3:
        game_start = False
        break

if player_score > computer_score:
    print(">>>Congratulations %s, You won the game!! <<<"
          "\n               😄😄😄" % player_name)
else:
    print(">>> You lost, computer won!!  <<< \n"
          "  >>> Better luck next time <<<\n"
          "              😣😣😣")

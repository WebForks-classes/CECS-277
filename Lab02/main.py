
'''
Group: 3
Author: Samuel Lara and Ethan Liu
Date: 8/24/22
Description: A program that...
'''
import random
import check_input

def weapon_menu():
    weapon_choice = input("Choose which weapon to use:\n R: Rock \n S: Scissors \n P: Paper \n B: Back \n")
    if weapon_choice == "R":
        return "R"
    elif weapon_choice == "S":
        return "S"
    elif weapon_choice == "P":
        return "P"
    elif weapon_choice == "B":
        return "B"
    else:
        print("Invalid input - should be a 'R', 'S', or 'P'.")


def comp_weapon():
  weapon_list = random.randint(1, 3)
  if weapon_list == 1:
    return "R"
  elif weapon_list == 2:
    return "S"
  elif weapon_list == 3:
    return "P"

def find_winner(player, comp):
    if comp == "B" or player == "B":
      return int(3)
    elif player == comp:
      print("Tie")
      return 0
    elif player == "R" and comp == "S":
        print("Player Wins")
        return int(1)
    elif player == "R" and comp == "P":
        print("Computer Wins")
        return int(2)
    elif player == "S" and comp == "R":
        print("Computer Wins")
        return int(2)
    elif player == "S" and comp == "P":
        print("Player Wins")
        return int(1)
    elif player == "P" and comp == "R":
        print("Player Wins")
        return int(1)
    elif player == "P" and comp == "S":
        print("Computer Wins")
        return int(2)
    else:
        return "Invalid input - should be a R, S, or P"


def display_score(player, comp):
  print("Player = " + str(player))
  print("Computer = " + str(comp))

def main():
  player = 0
  comp = 0
  start = True
  while start:
    user_input = check_input.get_int_range("RPS Menu:\n 1: Play Game \n 2: Show Score \n 3: Quit \n", 1, 3)
    if user_input == 1:
      battle = True
      while battle:
        user_weapon = weapon_menu()
        computer_weapon = comp_weapon()
        winner = find_winner(user_weapon, computer_weapon)
        # increments the winners score by 1
        if winner == 1:
          player += 1
        elif winner == 2:
          comp += 1
        elif winner == 3:
          battle = False
        
    elif user_input == 2:
      score = display_score(player, comp)
      print(score)
    elif user_input == 3:
      break

if __name__ == "__main__":
  main()

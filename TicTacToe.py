#-----GLOBAL VARIABLES-----


# Game board 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",
        ]

#if game is still going
game_still_going = True

# who won? or tie?
winner = None

#Whose turn is this
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])




def play_game():

    #display initial board
    print("\n")
    display_board()


    while game_still_going: 

      # handle a single of an arbitrary player
      handle_turn(current_player)

      # check if the game is over
      check_if_game_over()

      # Flip to the other player
      flip_player()

      # The game has ended 
      if winner == "X" or winner == "O":
        print(winner + " won.")
      elif winner == None and game_still_going == False:
        print("Tie")


def handle_turn(player):
  print("\n" + player + "'s turn")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1 

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again")

  

  board[position] = player
  
  print("\n")
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  #Set up global variable
  global winner


  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_colums()
  #check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner

  elif column_winner:
    winner = column_winner

  elif diagonal_winner:
    winner = diagonal_winner 


  return  

def check_rows():

  # Set up global variables 
  global game_still_going

  # check if 
  row_1 = board[0] == board[1] == board[2] != "-" 
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False

  # Return the winner (X or O)
  if row_1:
    return board[0]    
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_colums():

  # Set up global variables 
  global game_still_going

  # check if any of the rows have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-" 
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False

  # Return the winner (X or O)
  if column_1:
    return board[0]    
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():

    # Set up global variables 
  global game_still_going

  # check if 
  diagonals_1 = board[0] == board[4] == board[8] != "-" 
  diagonals_2 = board[6] == board[4] == board[2] != "-"
 

  # If any row does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False

  # Return the winner (X or O)
  if diagonals_1:
    return board[0]    
  elif diagonals_2:
    return board[6]
  

  return     

def check_if_tie():
  global game_still_going

  if "-" not in board:
    game_still_going = False

  return


def flip_player():

  # global variable
  global current_player
  # If the current player was X, then change it to O
  if current_player == "X":
    current_player = "O"
  # If the current player was O, then change it to X 
  elif current_player == "O":
    current_player = "X"

  return

play_game()
 



# board
# display board
# play game
# handle turn
# check if game over
    #check if win
        # check rows
        # check columns 
        # check diagonals
    # check if tie
# flip player

























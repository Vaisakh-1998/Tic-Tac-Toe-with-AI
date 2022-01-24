from random import choice

print("Welcome to Tic Tac Toe")
print("-----------------------\n")
 
      
dic = {"a":" ", "b":" ", "c":" ",
       "d":" ", "e":" ", "f":" ",
       "g":" ", "h":" ", "i":" "}


def dic_reset():
  for ke in list(dic.keys()):
    dic[ke] = " "
  

def board():
  # prints the board and positions  
  print(dic["a"]+"|"+dic["b"]+"|"+dic['c'],end="  ")
  print("a"+"|"+"b"+"|"+'c')
  print("-----",end = "  ")
  print("-----")
  print(dic['d']+"|"+dic['e']+"|"+dic['f'],end = "  ")
  print('d'+"|"+'e'+"|"+'f')
  print("-----",end = "  ")
  print("-----")
  print(dic['g']+"|"+dic['h']+"|"+dic['i'],end = "  ")
  print('g'+"|"+'h'+"|"+'i')
  print("\n")  


def com_play():      
  for p in ["O", "X"]:
    for ke in dic:
      if dic[ke] == " ":
        dic[ke] = p
        if win(dic):
          dic[ke] = "O"         
          return dic
        else:
          dic[ke] = " "       
  while True:
    position = choice(list(dic.keys()))  
    if dic[position] == " ":
      dic[position] = "O"
      break


def hum_play():  
  try:
    position = input("your turn\nwhat\'s your position: ")
    if dic[position] != " ":
      print("not playable position")
      hum_play() 
    else:                       
      dic[position] = "X"            
  except:
    print("invalid input")
    hum_play()


def win(d):  
  val = list(d.values())
  #horizondal  exmp(val[0:3])
  for i in range(0,7,3): 
    if val[i] != ' ' and len(set(val[i:i+3])) == 1:
      return val[i]
  #vertical  exmp(val[0], val[3], val[6])
  for i in range(3):
    if val[i] == val[i+3] == val[i+3*2] != " ":
      return val[i]
  #diagonal  exmp(val[0],val[4],val[8]) | val[2],val[4],val[6]
  for i in range(0, 3, 2):
    k = 4 - i
    if val[i] == val[i+k] == val[i+k*2] != " ":
      return val[i]   
  if " " not in val:
    return 0


def start_game(): 
  print("Start Game")
  print("----------\n")  
  board()
  player = 2
  for i in range(9):
    player = (player % 2) + 1
    if player == 1:
      hum_play()
    else: 
      com_play() 
    board()
    if win(dic) == "X":
      return "congrats you win the game"       
    elif win(dic) == "O":
      return "computer win the game\nbetter luck next time"
    elif win(dic) == 0:
      return "game draw"
    

if __name__ == "__main__":
  print(start_game())
  print()
  #restart game
  try:
    exit = input("yes for exit game, no for start next game\nyes/no:")
    exit = exit.lower()
  except:
    print("invalid input")      
  if exit == "no":
    dic_reset()
    print(start_game())
  else:
    print("game over")
  
    
    
    

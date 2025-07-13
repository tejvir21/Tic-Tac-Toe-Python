'''Tic Tac Toe Game'''
from colorama import Fore
from time import *

while True:

  l1=['1','2','3']
  l2=['4','5','6']
  l3=['7','8','9']
  
  turn_count=0
  
  while turn_count < 9:
    if turn_count >= 9:
      continue
    st1=' '
    for i in range(2):
      st1+=l1[i]
      st1+="  |  "
    st1+=l1[2]
    
    print(st1)
    
    print("---------------")
    
    st2=' '
    for j in range(2):
      st2+=l2[j]
      st2+="  |  "
    st2+=l2[2]
    
    print(st2)
    
    print("---------------")
    
    st3=' '
    for k in range(2):
      st3+=l3[k]
      st3+="  |  "
    st3+=l3[2]
    
    print(st3)
    
    print()
    
    player_one_choice=input(Fore.RED+"Player 1 Turn: ")
    if player_one_choice in l1:
      for i in range(3):
        if l1[i]==player_one_choice:
          l1[i]='X'
    
    elif player_one_choice in l2:
      for i in range(3):
        if l2[i]==player_one_choice:
          l2[i]='X'
    
    elif player_one_choice in l3:
      for i in range(3):
        if l3[i]==player_one_choice:
          l3[i]='X'
    
    else:
      print()
      print("Please Enter a valid Input!!!")
      print()
      continue
    
    print(Fore.RESET)
    
    st1=' '
    for i in range(2):
      st1+=l1[i]
      st1+="  |  "
    st1+=l1[2]
    
    print(st1)
    
    print("---------------")
    
    st2=' '
    for j in range(2):
      st2+=l2[j]
      st2+="  |  "
    st2+=l2[2]
    
    print(st2)
    
    print("---------------")
    
    st3=' '
    for k in range(2):
      st3+=l3[k]
      st3+="  |  "
    st3+=l3[2]
    
    print(st3)
    
    turn_count+=1

    if l1[0]==l2[0] and l1[0]==l3[0]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[0]==l2[1] and l1[0]==l3[2]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[0]==l1[1] and l1[0]==l1[2]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[1]==l2[1] and l1[1]==l3[1]:
      print()
      if l1[1]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[2]==l2[2] and l1[2]==l3[2]:
      print()
      if l1[2]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l2[0]==l2[1] and l2[0]==l2[2]:
      print()
      if l2[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l3[0]==l3[1] and l3[0]==l3[2]:
      print()
      if l3[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[2]==l2[1] and l1[2]==l3[0]:
      print()
      if l1[2]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    
    if turn_count==9:
      continue
    
    print()
    
    player_two_choice=input(Fore.BLUE+"Player 2 Turn: ")
    if player_two_choice in l1:
      for i in range(3):
        if l1[i]==player_two_choice:
          l1[i]='O'
    
    elif player_two_choice in l2:
      for i in range(3):
        if l2[i]==player_two_choice:
          l2[i]='O'
    
    elif player_two_choice in l3:
      for i in range(3):
        if l3[i]==player_two_choice:
          l3[i]='O'
    else:
      exit("Wrong Input!!!!")

    if l1[0]==l2[0] and l1[0]==l3[0]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[0]==l2[1] and l1[0]==l3[2]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[0]==l1[1] and l1[0]==l1[2]:
      print()
      if l1[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[1]==l2[1] and l1[1]==l3[1]:
      print()
      if l1[1]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[2]==l2[2] and l1[2]==l3[2]:
      print()
      if l1[2]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l2[0]==l2[1] and l2[0]==l2[2]:
      print()
      if l2[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l3[0]==l3[1] and l3[0]==l3[2]:
      print()
      if l3[0]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break
    elif l1[2]==l2[1] and l1[2]==l3[0]:
      print()
      if l1[2]=='X':
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 1 Won 🤩🏆")
        break
      else:
        print(Fore.LIGHTGREEN_EX+"🏆🤩 Player 2 Won 🤩🏆")
        break

    
    turn_count+=1
    
    print(Fore.RESET)
    
    continue
  else:
    print()
    print(Fore.CYAN+"👏 It's a Draw 👏")
  
  print()
  
  replay=input(Fore.RESET+"You want to play again[y/n]: ")
  if replay=='y' or replay=='Y':
    continue
  else:
    break

print()
print()

print(Fore.BLACK + "********",
      Fore.BLUE + "Thanks for playing the game 'TicTacToe'",
      Fore.BLACK + "********")
print(Fore.BLACK + "**********",
      Fore.LIGHTBLUE_EX + "Game Developer Tejvir Chauhan",
      Fore.BLACK + "**********")

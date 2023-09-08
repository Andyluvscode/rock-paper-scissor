import random

def getUserchoice():
  print("1 for rock, 2 for paper, or 3 for scissors?")
  choose=int(input())
  return choose

def getComputerChoice():
  list=[1,2,3]
  choice=random.choice(list)
  return choice 

def compareChoice(choose, choice):
  result=''
  if choose =="1" and choice == "1" :
    result='it is a tie'
  elif choose =='1' and choice =='2':
    result='you lost'
  elif choose =='1'and choice =='3':
    result='you won'
  elif choose=='2'and choice =='1':
    result='you won'
  elif choose =='2' and choice =='2':
    result='it is a tie'
  elif choose=='2'and choice =='3':
    result='you lost'
  elif choose =='3'and choice =='1':
    result='you lost'
  elif choose =='3' and choice =='2':
    result='you won'
  elif choose =='3' and choice =='3':
    result='it is a tie'
  return result
    

def printChoice (choose, choice, result):
  print("you chose")
  if choose==1:
    print('rock')
  elif choose ==2:
    print('paper')
  elif choose ==3:
    print('scissors')
  print('the computer got')
  if choice==1:
    print('rock')
  elif choice ==2:
    print('paper')
  elif choice ==3:
    print('scissors')  
  print('the result is')
  print(result)
  return (choose, choice, result)
def updateScores(wins, losses, ties, winner):
  if winner == 'it is a tie':
    ties=+1
  elif winner == 'you lost':
    losses=+1
  elif winner =='you won':
    wins=+1
  return wins, losses, ties
def PrintScores(wins,losses,ties):
  print('your score',wins)
  print('the computers score', losses)
  print('your ties', ties)
scores=[0,0,0]
while True:
  user= getUserchoice()
  comp= getComputerChoice()
  compare=compareChoice(user, comp)
  printChoice (user, comp, compare)
  scores=updateScores(scores[0], scores[1], scores[2], compare)
  PrintScores(scores[0],scores[1] ,scores[2])



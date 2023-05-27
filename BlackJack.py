from art import logo
from os import system
import random


Play_again=True

def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def calculate_score(cards):

  if(11 in cards and 10 in cards and len(cards)==2):
    return 0

  elif(11 in cards and sum(cards)>21):
    cards[cards.index(11)]=1
  
  return sum(cards)

def compare(user_score,computer_score):
  
  if(user_score==computer_score):
    print("It's a draw")
  elif(user_score==0):
    print("User has won")
  elif(computer_score==0):
    print("Opponent has a blackjack and he has won")
  elif(user_score>21):
    print("You went over you lost")
  elif(computer_score>21):
    print("Opponent went over you win")
  elif(computer_score>user_score and computer_score<=21 and user_score<21):
    print("You Lose")
  elif(computer_score<user_score and computer_score<21 and user_score<=21):
    print("You win")

while(Play_again==True):
  system('cls')
  print(logo)
  is_game_over=False
  user_cards = []
  computer_cards = []
  for i in range(0,2,1):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while(not is_game_over):
    
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f" Your cards: {user_cards},current score : {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    
    if(user_score==0 or computer_score==0 or user_score > 21):
      
      is_game_over = True
    else:
  
      user_should_deal = input("Type 'y' to draw another card: ")
      if(user_should_deal=='y'):
        user_cards.append(deal_card())
      else:
        is_game_over=True
    
  while(computer_score!=0 and computer_score<17):
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
    
  print(user_score,computer_score)
  
  compare(user_score,computer_score)
  Play=input("Do you want to play again if yes click 'y' else click 'n': ")
  if(Play=='y'):
    Play_again=True
  else:
    Play_again=False
print("Thank You for playing black jack")
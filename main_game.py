import random
import sys
import time

def select_statement(answer : str):
    match answer:
     case "yes":
      print("Ok lets play")
     case "no":
      print("Bye")
      return False
      sys.exit(0)
     case _:
      print("Please enter yes or no")
      return True
     
def roll_dice():
    return random.randint(1,6)
def get_choice():
    return input("Enter your choice (yes/no) : ")
    
def start_game(name : str):
 start = 0
 scrolls = int(input("How many scrolls do you want to do? : "))
 print(f"You have {scrolls} scrolls left")

 while start < scrolls:
  
   guess_number  = int(input("Guess a number between 1 and 6: "))
   while guess_number > 6 or guess_number < 1:
       print("Please enter a number between 1 and 6")
       return
   else:
     time.sleep(1)
     print("Rolling the dice...")
     roll_dice()
     time.sleep(1)
     if guess_number == roll_dice():
        print("You guessed right!")
     else:
        print("You guessed wrong!")
        
     start += 1   
     print(f"You have {scrolls - start} scrolls left")   
     
     if start == scrolls:
        back_again = str(input("Do you want to play again?(yes/no) : "))
        match back_again:
             case "yes":
              start_game(name)
             case "no":
              print("Bye {name}")
              return False
              sys.exit(0)
             case _:
              print("Please enter yes or no")
              return True
        break
    

def main():

  
 print("Hello and welcome to dice game!")

 name = input("What is your name? ")

 print(f"Hello {name}!")
    
 answer = str(input("Do you want to play?(yes/no): ")) 
 
 select_statement(answer)
 if not select_statement(answer):
    start_game(name)
 else:
    exit(0)
    
                
if __name__ == "__main__":
   main()
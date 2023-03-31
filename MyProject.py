from random import randint
import time
import os

def oantuxi():
 print("Wellcome to my the game rock-paper-scissors")
 print("Chao Mung Bạn Đến Với Trò Oẳn Tù Tì")
 # 0 = kéo ; 1 = búa ; 2 = bao
 player = input("Player Choose:" )
 computer = randint(0,2)
 if computer == 0:
     print("Computer Choose: keo") # Kéo
 if computer == 1:
     print("Computer Choose: bua")   # Búa
 if computer == 2:
     print("Computer Choose: bao")      # Bao
     
 if player == "keo":
     if computer == 0:
         print("Draw")
     if computer == 1:
         print("Lost")
     if computer == 2:
         print("Win")
 elif player == "bua":
     if computer == 0:
         print("Win")
     if computer == 1:
         print("Draw")
     if computer == 2:
         print("Lost")
 elif player == "bao":
     if computer == 0:
         print("Lost")
     if computer == 1:
         print("Win")
     if computer == 2:
         print("Draw")
 print("Play again?(yes/no): ")
 choose = input()
 if choose == "yes":
     return oantuxi()
 elif choose == "no":
     return menu()
 else:
     print("Vo li qua, exit thoi:v")
     exit()
     return 
     
     
def menu(): #The First Menu
    os.system("cls")
    print("1: rock-paper-scissors")
    print("2:...update")
    print('Select Number You Want: ')
    select = input()
    if select == 1:
        oantuxi()
    else:
        print("No, Pls Choose Again...")
        time.sleep(2)
        return

menu()


    


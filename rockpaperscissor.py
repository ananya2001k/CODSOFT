#Task4- Program to create rock paper scissors game
import random
print("*****Welcome to Rock-Paper-Scissors game*****")
cont=1
round=1
user_score=0
comp_score=0
print("Instructions/Rules of the game:")
print("Enter 0 for rock")
print("Enter 1 for paper")
print("Enter 2 for scissor")
choices=['0','1','2']
while(cont):
    print("***Round ",round," begins***")
    print("Enter you choice:")
    user=int(input("User:"))
    comp=int(random.choice(choices))
    print("Computer's choice is:",comp)
    if((user==0 and comp==0) or (user==1 and comp==1) or (user==2 and comp==2)): #rock-rock,paper-paper,scissor-scissor
        print("There's a tie")
    if(user==0 and comp==1):#rock-paper
        print("Computer wins")
        comp_score=comp_score+1
    if(user==0 and comp==2):#rock-scissor
        print("User wins")
        user_score+=1
    if(user==1 and comp==2):#paper-scissor
        print("Computer wins")
        comp_score+=1
    if(user==1 and comp==0):#paper-rock
        print("User wins")
        user_score+=1
    if(user==2 and comp==0):#scissor-rock
        print("Computer wins")
        comp_score+=1
    if(user==2 and comp==1):#scissor-paper
        print("User wins")
        user_score+=1
    print("Enter 1 if you want to continue and 0 if you want to exit")
    ch=int(input())
    if(ch==1):
        cont=1
        round+=1
    else:
        cont=0
print("The final scores are:")
print("User:",user_score)
print("Computer:",comp_score)
if(user_score > comp_score):
    print("User wins")
else:
    print("Computer wins")
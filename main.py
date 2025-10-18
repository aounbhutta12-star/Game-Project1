import random

'''

-1 for snake
1 for water
0 for gun

'''

computer=random.choice([-1,0,1])
user=input("ENTER THE WORD OF YOUR CHOICE: ")

# now as we want to tell the program that
                       #   which word  = which value, for that we will create a dictionary

userdict={

    "w":1,

    "s":-1,

    "g":0
}             
reversedict={
    1:"WATER",
    
   -1:"SNAKE",
    
    0:"GUN"
    
}     

# we just we reverse dict to inform the user that what key 
# he has pressed and what the computer chose

you=userdict[user]



print(f"YOU CHOSE {reversedict[you]} THE COMPUTER CHOSE {reversedict[computer]}")

if(computer==you):
    print("It's a Draw!")

else:
     if(computer==1 and you==-1):
        print("AJ TOU WIN HAI!🏆🔥")
        
     elif(computer==-1 and you==1):
        print("APKO LEARN MIL GYA!🤓")

     elif(computer==1 and you==0):
        print("AJ TOU WIN HAI!🏆🔥")

     elif(computer==0 and you==1):
        print("APKO LEARN MIL GYA!🤓")

     elif(computer==-1 and you==0):
        print("AJ TOU WIN HAI!🏆🔥")

     elif(computer==0 and you==-1):
        print("APKO LEARN MIL GYA!🤓")

     else: 
        print("YOU ENTERD THE WRONG KEY")



        
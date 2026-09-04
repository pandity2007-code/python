import random

def game():
    print(" you are plaYING a game")
    score=random.randint(1,100) 
    #fetch the hiscore with file
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0    
    print(f"the score is {score}")
    #write high score to file
    if (score>hiscore ):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()
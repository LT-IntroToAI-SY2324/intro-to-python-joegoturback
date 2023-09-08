import random
playerchoice = input(' enter rock, paper, or scissors: ')
print("your choice: " + playerchoice)
def get_choices():
    options = ['rock', 'paper', 'scissors']
    computerchoice = random.choice(options)
    print('Computer choice: ' + computerchoice)
    return computerchoice


compchoice = get_choices()

def getWinner():
    playerwon = "you win"
    compwon = 'computer wins'
    draw = "tie!"
    if (playerchoice == "scissors" and compchoice == "paper") or (playerchoice == 'paper' and compchoice == 'rock') or (playerchoice == 'rock' and compchoice == 'scissors'):
        return playerwon
    elif  (compchoice == "scissors" and playerchoice == "paper") or (compchoice == 'paper' and playerchoice == 'rock') or (compchoice == 'rock' and playerchoice == 'scissors'):
        return compwon
    else:
        return draw 

whoWon = getWinner()
print(whoWon)
 
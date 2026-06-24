import random
list = ['rock', 'paper', 'scissors']
player_points = 0
cpu_points = 0

print("Welcome to Rock Paper Scissors!")
while True:
    cpu = random.choice(list)
    print(f"\nScore is (CPU {cpu_points} : Player {player_points})")
    player = (input("Say Rock, Paper or Scissors!\n")).lower().strip()
    if player != 'rock' and player != 'paper' and player != 'scissors':
        print("Uh oh, you might of had a slight mistype")
    elif cpu == player:
        print("Uh oh, tie! Try again!\nYou both chose " + player + '!')
    elif (player == 'rock' and cpu == 'scissors') or (player == 'scissors' and cpu == 'paper') or (player == 'paper' and cpu == 'rock'):
        print("You win! Yay!\nYou beat the " + cpu + " with your " + player + "!" )
        player_points += 1
    else:
        print("You lose! Womp womp!\nThe computer won with " + cpu + "!" )
        cpu_points += 1
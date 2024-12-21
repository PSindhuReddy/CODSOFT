import random
print('🎮Welcome to the Rock, Paper, Scissors game!🎮')
print('In this game, you will compete against the 🖥️')
print('You will make your choice from the following:')
print('  - 🪨 (r): Crushes ✂️')
print('  - 🗒️ (p): Covers 🪨')
print('  - ✂️ (s): Cuts 🗒️')
print('You will play 5 rounds. Let\'s see who wins the most rounds!')
print(" ✨Good luck!!Get ready for the adventure of a lifetime!✨")
word = ['r', 'p', 's']
player_score = 0
system_score = 0
for _ in range(5):
    a = input("\nYour turn! Choose one: Rock (r), Paper (p), or Scissors (s): ").lower()
    if a not in word:
        print('Oops! That\'s not a valid choice. Please choose "r" for Rock, "p" for Paper, or "s" for Scissors.')
        continue
    b = random.choice(word)
    print(f'\nThe system chose: {b}')
    if (a == 'r' and b == 's') or (a == 'p' and b == 'r') or (a == 's' and b == 'p'):
        player_score += 1
        print("You win this round! 🎉")
    elif (b == 'r' and a == 's') or (b == 'p' and a == 'r') or (b == 's' and a == 'p'):
        system_score += 1
        print("You lose this round. 😞")
    else:
        player_score += 1
        system_score += 1
        print("It's a draw for this round. 😐")

# Display final results
print(f'\nYour final score: {player_score}')
print(f'System\'s final score: {system_score}')

if player_score > system_score:
    print(f'🎉 Congratulations! You won the game by {player_score - system_score} points! 🎊')
elif player_score == system_score:
    print('It\'s a draw! Well played! 😐')
else:
    print(f'You lost the game. Better luck next time! 🙁')

import random
words=["Apple","house","tiger","table","chair","happy","ocean","shadow","forest","winter","music","garden","bottle","play"]
chosen_word=random.choice(words)


display=[]
print("Welcome to the Hangman Game\nYou only have 6 lives to guess the correct word\nLet's Start the Game")


def hangman(hang):
    stages = [
        "+__________+\n |       |\n         |\n         |\n         |\n         |\n_________|",
        "+__________+\n |       |\n O       |\n         |\n         |\n         |\n_________|",
        "+__________+\n |       |\n O       |\n |       |\n         |\n         |\n_________|",
        "+_________+\n |       |\n O       |\n/        |\n         |\n         |\n_________|",
        "+_________+\n |       |\n O       |\n/|\\      |\n         |\n         |\n_________|",
        "+_________+\n |       |\n O       |\n/|\\      |\n/        |\n         |\n_________|",
        "+_________+\n |       |\n O       |\n/|\\      |\n/ \\      |\n         |\n_________|"
    ]
    print(stages[hang])


lives=6
hang=0

print("Fill all the gaps with correct letters")
for i in range(len(chosen_word)):
     display+='_'
print(display)


game_over=False
while(game_over==False):
     guessed_letter=input("Guess a letter:").lower()
     if guessed_letter in chosen_word:
         for i in range(len(chosen_word)):
            if chosen_word[i]==guessed_letter:
                  display[i]=guessed_letter
                  print("Correct!")

         print(display)
         hangman(hang)


     else:
        lives-=1
        hang+=1
        print(f"Wrong! You have {lives} lives left")
        print(display)
        hangman(hang)


     if '_' not in display:
        game_over=True
        print("Congrats!You won")
     elif(lives==0):
        game_over=True
        print("You loose")
        print(f"The word was {chosen_word}")





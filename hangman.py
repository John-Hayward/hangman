import requests
from random_word import RandomWords

r=RandomWords()

print("Hangman Game")

target_word=r.get_random_word(minLength=4, maxLength=10, hasDictionaryDef="true")
target_arr=[]
for letter in target_word:
    target_arr.append(letter)
guessed_arr=["_"]*len(target_word)


lives=10

def guess(letter, target_array, guessed_array):
    for i in range(len(target_array)):
        if target_array[i]==letter:
            guessed_array[i]=letter

    return letter in guessed_arr

print(" ".join(guessed_arr) + "\n")
print(f"Starting lives: {lives} \n")

while lives>0:
    current_guess=input("Guess a letter ").strip().lower()

    if len(current_guess)!=1:
        print("Invalid guess, please enter one character")
        pass

    guess(current_guess,target_arr,guessed_arr)

    if not guess(current_guess,target_arr,guessed_arr):
        lives -=1 

    print(" ".join(guessed_arr) + "\n")
    print(f"Remaining lives: {lives} \n")

    if guessed_arr==target_arr:
        print("YOU WIN!")
        break

if lives==0:
    print(f"The word was {target_word}")

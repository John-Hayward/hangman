print("Hangman Game")

target_word="rhythm"
target_arr=[]
for letter in target_word:
    target_arr.append(letter)
guessed_arr=["_"]*len(target_word)
lives=10

def guess(letter, target_array, guessed_array):
    for i in range(len(target_array)):
        if target_array[i]==letter:
            guessed_array[i]=letter

print(" ".join(guessed_arr))
guess("r",target_arr,guessed_arr)
print(" ".join(guessed_arr))
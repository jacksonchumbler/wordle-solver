from english_words import english_words_lower_set
five_letters = []
for word in english_words_lower_set:
    if len(word) == 5:
        five_letters.append(word)


def suggest_word(candidates):
    guesses = [] #contains [{"guess", #cor, #wrong}]
    guess = input("What was your guess (e to quit)")
    correct_indx = []
    wrong_spot_indx = []
    #while(guess != "e"):
    num_correct = int(input("How many did you get in the right spot? "))
    if(num_correct > 0):
        for i in range(num_correct):
            indx = input("Enter an index: ")
            correct_indx.append(indx)
    num_wrong_spot = int(input("How many in the wrong spot? "))
    if(num_wrong_spot > 0):
        for i in range(num_wrong_spot):
            indx = input("Enter an index: ")
            wrong_spot_indx.append(indx)
    guesses.append([guess, correct_indx, wrong_spot_indx])
    correct_indx = []
    wrong_spot_indx = []
    #guess = input("What was your guess (e to quit)")
    #Now, we have all guesses and correctness

    #Whittle all words without correct index
    to_remove = []
    for word in candidates:
        for guess in guesses:
           #Correct Spot
            removed = False
            for i in guess[1]:
                if word[int(i)] != guess[0][int(i)]:
                    if word not in to_remove:
                        to_remove.append(word)
                    removed = True
                    break
            #Wrong Spot
            if removed:
                break
            for i in guess[2]:
                if guess[0][int(i)] not in word:
                    if word not in to_remove:
                        to_remove.append(word)
                    break
                elif guess[0][int(i)] == word[int(i)]:
                    if word not in to_remove:
                        to_remove.append(word)
                    break
            #Incorrect Letters
            
            incorrect_letters = ['0','1','2','3','4']
            incorrect_letters = [item for item in incorrect_letters if item not in guess[1]]
            incorrect_letters = [item for item in incorrect_letters if item not in guess[2]]

                    
            #if word == "truce":
                #print(guess[1])
                #print(guess[2])
                #print(incorrect_letters)
            for i in incorrect_letters:
                if guess[0][int(i)] in word:
                    if word not in to_remove:
                        to_remove.append(word)
                    break     
            
    for word in to_remove:
        candidates.remove(word)
    return candidates

 
candidates = five_letters
candidates = suggest_word(candidates)
print(candidates)
user_inp = input("Add Another? (e to quit)")
while(user_inp != "e"):
    candidates = suggest_word(candidates)
    print(candidates)
    user_inp = input("Add Another? (e to quit)")
print(candidates)


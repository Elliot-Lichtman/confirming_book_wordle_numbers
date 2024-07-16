word_list = ["adept", "after", "tread", "agent", "avert", "tweak", "cater", "eaten", "eater", "extra", "hater", "taker", "taken", "water", "taper", "great", "wheat", "treat"]


## HELPER FUNCTIONS ##
#############################
def count_letter(letter, word):
    count = 0
    for c in word:
        if c == letter:
            count += 1
    return count

# converts a list to a string
def ltos(list):
    s = ""
    for item in list:
        s += str(item)
    return s
#############################


## SCORE FUNCTION
#############################
# (I'm pretty sure this is fully correct, but I checked that it agrees on everything in this test)
def score(guess, word):

    # 0 is gray, 1 is yellow, 2 is green
    score = [0, 0, 0, 0, 0]

    # keep track of how many times we've scored each letter
    scored_letters = {}
    for i in range(len(guess)):
        scored_letters[guess[i]] = 0    

    # first do the greens
    for i in range(len(guess)):
        if guess[i] == word[i]:
            score[i] = 2
            scored_letters[guess[i]] += 1
        
    # now fill in the yellow scores
    for i in range(len(guess)):
        if scored_letters[guess[i]] < count_letter(guess[i], word) and score[i] != 2:
                scored_letters[guess[i]] += 1
                score[i] = 1
    
    return ltos(score)
###############################

## Function to find average # of words left after a guess
def find_words_left(guess):
    score_counts = {}

    for word in word_list:
        would_be_score = score(guess, word)

        print(word, score(guess, word))

        if would_be_score not in score_counts:
            score_counts[would_be_score] = 1
        else:
            score_counts[would_be_score] += 1
    
    total = 0

    for bucket in score_counts:
        total += score_counts[bucket]**2
    
    print(score_counts)

    return (total-1)/len(word_list)
    
    
print(find_words_left("water"))

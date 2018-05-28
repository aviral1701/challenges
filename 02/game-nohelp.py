#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7

def pick_letters():
	indices = [random.randint(0,len(POUCH)-1) for x in xrange(7)]
	return [POUCH[i] for i in indices]

def validate(word,lis):
	#all letters of word are in draw
	result = True
	for i in xrange(len(word)):
		result = result and (word[i].upper() in lis)
	# word is valid
	result=result and word in DICTIONARY
	return result

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
   		word =  max(words, key=calc_word_value)
   		word = ''.join(word)
		return word


def main():
	#draw seven letters
    draw = pick_letters()
    print("Use this letters to make a word:",draw)

    while True:
    	user_word = raw_input()
    	user_word = user_word.lower()
    	if validate(user_word,draw)==True:
    		break

    print("Your score: ",calc_word_value(user_word))

    allperm = []

    for i in xrange(7):
    	for j in xrange(i,7):
    		temp_letters = draw[i:j]
    		temp_words = list(itertools.permutations(temp_letters))
    		for x in temp_words:
    			temp_word = ''.join(x)
    			if temp_word.lower() in DICTIONARY:
    				allperm.append(temp_word)

    max_word = max_word_value(allperm)
    print(max_word)


if __name__ == "__main__":
    main()

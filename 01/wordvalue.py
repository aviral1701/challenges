from data import DICTIONARY, LETTER_SCORES

def load_words():
	f = open(DICTIONARY,'r')
	text=f.read()
	word_list = text.split()
	return word_list

def calc_word_value(word):
    '''Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES'''
    value = 0
    for index in range(len(word)):
        try:
    	   value += int(LETTER_SCORES[word[index].upper()])
        except:
            pass
    return value
     

def max_word_value(word_list=load_words()):
    '''Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY'''
    max_value=0
    max_word='hello'
    for word in word_list:
    	temp=calc_word_value(word)
    	if max_value<temp:
    		max_value = temp
    		max_word = word
    return max_word
    
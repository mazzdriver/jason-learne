	
def get_words():
	word_to_solve = input('Введите слово, которое будут отгадывать: ')
	word_to_show = ['_' * len(word_to_solve)]
	return word_to_solve,word_to_show
	

	
def mainframe(attempt, word_to_solve, word_to_show):
	
	if attempt in word_to_solve:
		good = word_to_solve.index(attempt)
		word_to_show[good] = attempt
	
def win(word_given, word_got):
	if word_given == word_got:
		is_discovered = True

def bad_try(errors, attempt):
	errors += 1
	bad_letters.append(attempt)
	
	
hanging = ['\n\n\n\n', 
'\n \n \n/|\\', 
'\n |\n |\n |\n/|\\', 
'\n |¯¯¯\n |   \n |     \n/|\\', 
'\n |¯¯¯|\n |   \n |  \n/|\ ', 
'\n |¯¯¯|\n |   o\n |  \n/|\ ', 
'\n |¯¯¯|\n |   o\n |   |\n/|\ ', 
'\n |¯¯¯|\n |   o\n |  /|\n/|\ ', 
'\n |¯¯¯|\n |   o\n |  /|\\\n/|\ ', 
'\n |¯¯¯|\n |   o\n |  /|\\\n/|\ / ',
'\n |¯¯¯|\n |   o\n |  /|\\\n/|\ / \\\nПовесили :(']


		
	
is_playing = True
errors = 0
bad_letters = []

while is_playing:
	is_discovered = False
	word, showing_word = get_words()
	while not is_discovered:
		output = [showing_word, bad_letters, hanging[errors]]
		attempt = input('Какая буква есть в слове? Ваше предложение: ')
		if is_discovered:
			win(word, showing_word)
		else:
			bad_try(errors, attempt)
			
			
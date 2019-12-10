class Date:
    def __init__(self):
        """initialize all needed variables"""

        self.day = ""  # day of the month
        self.month = ""  # month of the year
        self.year = ""  # year
        self.symbols = []   # init list of symbols in transition matrix
        self.transition_matrix = []  # init transition matrix

def mealy(state, symbol):
	"""perform a mealy machine on our date"""

	# if state 0 and symbols[0], must be a capitol letter, add to month
	if state == 0 and symbol in Date.symbols[0]:
		Date.month += symbol
	# if state 1 and symbols[1], must be lowercase letter, add to month
	elif state == 1 and symbol in Date.symbols[1]:
		Date.month += symbol
	# if state 2, 3, or 4 and symbols[3], must be integer, add to day
	elif (state == 2 or state == 3 or state == 4) and symbol in Date.symbols[3]:
		Date.day += symbol
	# if state 6 and symbols[3], must be integer, add to year
	elif state == 6 and symbol in Date.symbols[3]:
                Date.year += symbol

def moore(state):
	pass

def transition(state,symbol):
	"""perform transitions through the matrix"""

        # put capitol letters in sym_index 0
	if symbol in Date.symbols[0]:
		sym_index = 0
	# put lowercase letters in sym_index 1
	elif symbol in Date.symbols[1]:
		sym_index = 1
	# put spaces in sym_index 2
	elif symbol in Date.symbols[2]:
		sym_index = 2
	# put integers in sym_index 3
	elif symbol in Date.symbols[3]:
		sym_index = 3
	# put commas in sym_index 4
	elif symbol in Date.symbols[4]:
		sym_index = 4
	else:
		sym_index = Date.symbols.index(symbol)

	# return state and sym_index
	return Date.transition_matrix[state][sym_index]

def initialize():
	"""this function will initialize all needed variables"""

	# init the day, month and year
	Date.day = ""
	Date.month = ""
	Date.year = ""

        # open the built transition matrix file, first line of file is symbols, second line is matrix.
	f = open("tm2.txt")
	Date.symbols = eval(f.readline())
	Date.transition_matrix = eval(f.readline())

	return 0

def output(is_valid):
	"""this function will display the output for us"""

	# this will print out the month, day, and year back to the user if valid.
	if is_valid:
		return 'Valid: %s %s, %s' % (Date.month, Date.day, Date.year)
	else:   # If not valid, return invalid
		return 'Invalid'





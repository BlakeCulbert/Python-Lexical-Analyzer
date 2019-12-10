import date_fsa as fsa

def choose():
    """Use this function to have the user choose to do test file or user input."""

    choice = input('File or User Input? (F/U): ')  # user input choice
    if choice == 'F':  # if choice is 'F' do the test file
       file()
    elif choice == 'U': # if choice is 'U' do user input
       user()

def file():
    """this is the function for the test file input"""

    f = open('dates.txt')
    # open the test text document in f.

    validcount = 0
    # init validcount for output
    invalidcount = 0
    # init invalidcount for output
    increcognized = 0
    # init incorrectly recognized for output

    for i in f:  # loop through all the file

        sentence2 = f.readline()
        # read the sentence into sentence2
        sentence = sentence2.replace("\n","")
        # use this to get rid of new line character since not in our symbols

        state = fsa.initialize()
        # init first state of the FSA
        is_valid = True
        # init is_valid to true, boolean

        for symbol in sentence:
        # take symbol and sentence
            fsa.mealy(state, symbol)
            # perform a mealy machine on our sentence
            state = fsa.transition(state, symbol)
            # transition from state to state
            if state == "":
            # if the symbol is incorrect in that state, sentence is invalid
               is_valid = False
               invalidcount+=1
               # add to invalidcount
               break;

        if is_valid == True:
        # when true, add to validcount/increcognized
            if len(fsa.Date.year) > 4:
            # if length of year more than 4 integers, increment incorrectly recognized
               increcognized+=1
            else:
               validcount+=1

    print()
    print('The Number of Correctly Recognized Sentences (Out of 150): ', validcount)
    # output valid count
    print()
    print('The Number of Invalid Sentences (Out of 150): ', invalidcount)
    # output invalid count
    print()
    print('The Number of Incorrectly Recognized (Out of 150): ', increcognized)
    # output incorrectly recognized
    print()

def user():
    """This function will take user input and verify if the sentence is in our language"""

    print()
    sentence = input('What is your sentence? (ex. May 02, 2019)  ')
    print()

    state = fsa.initialize()
    # Initialize the first state of the FSA.
    is_valid = True

    for symbol in sentence:
    # Take the symbol and sentence
        fsa.mealy(state, symbol)
        # Perform a mealy machine on the given sentence
        state = fsa.transition(state, symbol)
        # Transition state to state
        fsa.moore(state)
        # Peform a moore machine on the sentence
        if state == "":
        # If the sentence does not match our language, change is_valid to false.
            is_valid = False
            break;  # get out of the loop.

    output = fsa.output(is_valid)
    # set variable output to our output function in fsa.

    print()
    print(output)   # print output
    print()

    return



def main():
    """use main to start our program, run choose() to pick between user and file input"""

    choose()

if __name__ == "__main__":
    main()
from random import choice


def open_hidden_letter(choice_word, hidden_word, input_letters, c):
    i = 0

    if c in input_letters:
        print("You've already guessed this letter")
        return True
    else:
        if len(c) == 1 and c.islower():
            input_letters.append(c)
    if c not in choice_word:
        if len(c) != 1:
            print("You should input a single letter")
            return True
        if c.islower() == False:
            print("Please enter a lowercase English letter")
            return True
        print("That letter doesn't appear in the word")
        return False
    for each in choice_word:
        if each == c:
            hidden_word[i] = c
        i += 1
    return True


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
choice_word = choice(words)
hidden_word = []
input_letters = []
while 1:
    menu_choice = input('Type "play" to play the game, "exit" to quit:')
    if menu_choice == 'play':
        for x in range(len(choice_word)):
            hidden_word.append('-')
        lives = 8
        while lives:
            hidden_word_print = ''.join(hidden_word)
            print('\n' + hidden_word_print)
            c = input('Input a letter: ')
            if not open_hidden_letter(choice_word, hidden_word, input_letters, c):
                lives -= 1
            if ''.join(hidden_word) == choice_word:
                print('\n' + choice_word)
                print("You guessed the word!\nYou survived!\n")
                exit()
        print("You lost!\n")
    elif menu_choice == 'exit':
        exit()
    else:
        pass

import random

def get_word():
    words = ['Woodstock',
        'Gary',
        'Tucker',
        'Gopher',
        'Spike',
        'Ed',
        'Faline',
        'Willy',
        'Rex',
        'Rhino',
        'Roo',
        'Littlefoot',
        'Bagheera',
        'Remy',
        'Pongo',
        'Kaa',
        'Rudolph',
        'Banzai',
        'Courage',
        'Nemo',
        'Nala',
        'Alvin',
        'Sebastian',
        'Iago',
        'Zazu',
        'Diego',
        'Dory',
        'Pumbaa',
        'Rabbit',
        'Garfield',
        'Manny',
        'Chewbacca',
        'Sid',
        'Flik',
        'Marty',
        'Gloria',
        'Melman',
        'Alex',
        'Julien',
        'Wilbur',
        'Asian',
        'Droopy',
        'Simba',
        'Snoopy',
        'Mufasa',
        'Kerchak',
        'Scar',
        'Pete',
        'Balto',
        'Eeyore',
        'Piglet',
        'Donkey',
        'Timon',
        'Baloo',
        'Thumper',
        'Bambi',
        'Goofy',
        'Tom',
        'Sylvester',
        'Jerry',
        'Tigger']

    return random.choice(words).upper()

def check(word, guesses, guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print('Yes! The word contains',matches,'"' + guess + '"' + 's')
    elif matches == 1:
        print('Yes! The word contains the letter "' + guess + '"')
    else:
        print('Sorry. The word does not contain the letter"' + guess + '"')

    return status

def main():
    word = get_word()
    #print(word)
    guesses = []
    guessed = False ## boolean
    print('The word contains', len(word), 'letters.')
    failedCount = 0
    while not guessed:
        text = 'Please enter one letter or a {}-letter word. '.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
           print('Invalid entry.')

        if len(guesses) - len(word) > 7:
           print('You missed ' + str(len(guesses) - len(word)) + ' times, about to be hanged. Be careful')

    print('Yes, the word is', word + '! You got it in', len(guesses), 'tries.')

main()
     
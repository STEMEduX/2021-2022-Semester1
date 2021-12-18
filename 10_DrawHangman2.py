
import random

def h6():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |      /|\ ') 
    print('        |     / | \ ')
    print('        |') 
    print('      -----')

def h5():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |      /|') 
    print('        |     / | ')
    print('        |') 
    print('      -----')

def h4():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |       |')
    print('        |       |') 
    print('        |') 
    print('      -----')

def h3():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|') 
    print('        |       |')
    print('        |       |') 
    print('        |       | ')
    print('        |') 
    print('      -----')

def h2():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |       |') 
    print('        |       |')
    print('        |       |') 
    print('        |       |')
    print('        |') 
    print('      -----')

def h1():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h0():
    print('        _________')
    print('        |/      |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def hang(status):
        if status == 1:
            h1()
        elif status == 2:
            h2()
        elif status == 3:
            h3()
        elif status == 4:
            h4()
        elif status == 5:
            h5()
        elif status == 6:
            h6()
    
def main():

    while (True):
        text = 'Run a dice? (answer Y or N): '
        guess = input(text)
        if guess == 'Y':
            r = random.randrange(6)
            print('You rolled ' + str(r))
            hang(r)
        else:
            break


main()

def h11():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |      \|/') 
    print('        |       |')
    print('        |      /|\ ') 
    print('        |') 
    print('      -----')

def h10():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |      \|/') 
    print('        |       |')
    print('        |      /|') 
    print('        |') 
    print('      -----')

def h9():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |      \|/') 
    print('        |       |')
    print('        |       |') 
    print('        |') 
    print('      -----')

def h8():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |      \|') 
    print('        |       |')
    print('        |       |') 
    print('        |') 
    print('      -----')

def h7():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |       |') 
    print('        |       |')
    print('        |       |') 
    print('        |') 
    print('      -----')

def h6():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h5():
    print('        _________')
    print('        |/      |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h4():
    print('        _________')
    print('        |/')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h3():
    print('        _________')
    print('        |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h2():
    print('        _________')
    print('        |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 

def h1():
    print('        |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 

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
        elif status == 7:
            h7()
        elif status == 8:
            h8()
        elif status == 9:
            h9()
        elif status == 10:
            h10()
        elif status == 11:
            h11()
    
def main():

    while (True):
        text = 'Please enter one number less than 12: '
        guess = input(text)
        if guess == 0:
            break
        hang(int(guess))


main()
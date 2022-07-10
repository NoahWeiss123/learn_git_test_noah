#ROCK PAPER SIMULATOR GAME BY NOAH WEISS

space = 3
while space >= 0:
    print('')
    space = space - 1

x = 0
y = 0
z = 0

status = False

start = False
while start == False:
    print('')
    numofgames = input('How many games do you want to simulate? ')
    try:
        num = int(numofgames) - 1
        start = True
    except:
        print('')
        print('Enter a valid input')
        start = False

playsim = False
while playsim == False:
    print('')
    play1 = input("What play would you like to simulate? [R]ock [P]aper [S]cissors: ")
    if 'R' == play1.upper():
        print('You selected Rock')
        p = 'r'
        playsim = True
    elif 'P' == play1.upper():
        print('You selected Paper')
        p = 'p'
        playsim = True
    elif 'S' == play1.upper():
        print('You selected Scissors')
        p = 's'
        playsim = True
    if 'END' == play1.upper():
        status = False
        exit()
    if status != True:
        print('')
        print('Retry with a valid input')
        print('')
    
print('')
print('Welcome to Rock Paper Scissors!')
print('')

Start = True

while num >= 0:

    computer = 0
    player = 0
    gameplay = 0

    status = False

    while status == False:
        play = p
        print('')

        if 'R' == play.upper():
            print('You selected Rock')
            selection = 1
            status = True
        elif 'P' == play.upper():
            print('You selected Paper')
            selection = 2
            status = True
        elif 'S' == play.upper():
            print('You selected Scissors')
            selection = 3
            status = True

        if play.upper() == 'END':
            status == False
            exit()
    

        if status != True:
            print('')
            print('Retry with a valid input')
            print('')
    
    print('')

    import random

    random_number = random.randint(0, 10)

    if random_number <= 4:
        print('Computer selects Rock')
        comselec = 1
    elif random_number >= 4 and random_number <= 7:
        print('Computer selected Paper')
        comselec = 2
    elif random_number >= 7:
        print('Computer selected Scissors')
        comselec = 3
    print('')

    if comselec == selection:
        print('Tie')
        computer = 0
        player = 0
        gameplay = 1
    if selection == 1 and comselec == 2:
        print('Computer wins')
        player = 0
        computer = 1
        gameplay = 1
    if selection == 2 and comselec == 3:
        print('Computer wins')
        player = 0
        computer = 1
        gameplay = 1
    if selection == 3 and comselec == 1:
        print('Computer wins')
        player = 0
        computer = 1
        gameplay = 1
    if selection == 1 and comselec == 3:
        print('YOU WIN')
        player = 1
        computer = 0
        gameplay = 1
    if selection == 2 and comselec == 1:
        print('YOU WIN')
        player = 1
        computer = 0
        gameplay = 1
    if selection == 3 and comselec == 2:
        print('YOU WIN')
        player = 1
        computer = 0
        gameplay = 1

    print('')

    x = x + gameplay
    y = y + computer
    z = z + player

    print('Games played:', x)
    print('Computer wins', y)
    print('Player wins', z)
    print('')
    num = num - 1



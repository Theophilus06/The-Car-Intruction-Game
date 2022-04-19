print('THE CAR GAME (GIVING INSTRUCTIONS) ')
print('Type Help to Start')
command = ''
started = False
drive = False
turn_left = False
ture_right = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
          print('Car Already Started')
        else:
            started= True
            print('Car Started')
    elif command == 'drive':
        if drive:
            print('Driving Already')
        else:
            drive = True
            print('Driving')
    elif command == 'turn left':
        if turn_left:
            print('Car Has Already Turned Left')
        else:
            turn_left = True
            print('Car is Turning Left')
    elif command == 'turn right':
        if ture_right:
            print('Car Has Already turned Right')
        else:
            ture_right = True
            print('Car Turing Right')
    elif command == 'stop':
        if not started:
            print('Car Already Stopped')
        else:
            started = False
            print('Car Stopped')
    elif command == 'help':
        print('''
Options to Choose From:
Type: 
(*) Start: - To Start The Car
(*) Drive: - To Drive The Car
(*) Turn Right: - To Turn Right
(*) Turn Left: - To Ture Left
(*) Stop: - to Stop The Car
(*) Quit: - To Quit The Game
''')
    elif command == 'quit':
        print('Game Over')
        break
    else:
        print("Please Select Only From The Options Given")







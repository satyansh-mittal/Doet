# Doet
from time import sleep
def intro():
    print('\t\tWELCOME TO Doet')
    sleep(1)
    print('\n AN APP THAT CAN KEEP YOU REMINDED OF ALL YOUR DAILY, WEEKLY, MONTHLY OR YEARLY GOALS')
    sleep(1)
    print('\n THIS APP WILL KEEP YOU MOTIVATED AND KEEP TRACK OF YOUR GOALS ALL THE TIME')
    sleep(1)
    print('\n\n copywrite to Satyansh Mittal')
    input('Press any key to continue')


def mainProgram():
    run = True
    goalnumber = int(input('How many goals do you want to have: '))
    time = int(input('For how long do you want your goals to be showed(in seconds): '))

# writing goals
    print('\n Please write your goals below:-')
    list = []    
    for i in (0,goalnumber):
        run = input(f'Enter your goal{i}: ')
        list.append(run)

# displaying goals
    time_end = 0
    while time_end<=time:
        print('\nYOUR GOALS ARE:-')
        for x in list:
            print('-',x)
        print('\n\t\tYOU CAN DO IT🐱‍👤🐱‍👤🐱‍👤😾')
        print('\t\tKEEP GOING')
        
        sleep(1)
        time_end+=1

intro()
mainProgram()
ask = input('Do you want to set goals agian(yes/no): ')
if ask=='yes':
    mainProgram()
else: 
    print('THANK YOU FOR USING DOET')
    
        
    
        
        
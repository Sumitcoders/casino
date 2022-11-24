import random

br = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


print('''
********************************************************************************
|     |        |     ~~~~~~   |       ~~~~~~~     ~~~~~~~    |\    /|   ~~~~~~ |
|     |        |    |         |      |           |       |   | \  / |  |       |
|     |   /\   |    |~~       |      |           |       |   |  \/  |  |~~     |
|     |  /  \  |    |         |      |           |       |   |      |  |       |
|     |_/    \_|     ~~~~~~    ~~~~~  ~~~~~~~     ~~~~~~~    |      |   ~~~~~~ |
********************************************************************************


''')



names = []
price = []
n = int(input('Enter the number of players: '))

for i in range(n):
    name = input(f'Enter the name of person no. {i+1} : ')
    names.append(name)
    price.append(int(100))
turn = 0
dice = [1,2,3,4,5,6]
print(names)
while True:
    try:
        print(br)
        print('Turn for ', names[turn])
        print('Your balance: ', price[turn],'$')
        money = float(input('Enter the Bet Ammount: '))
        bet = input('Bet any two numbers (eg. 2 , 3): ')
        a = int(bet.split(',')[0])
        b = int(bet.split(',')[1])
        roll = random.choice(dice)
        if  roll == a or roll == b:
            print('you won your bet')
            c_price = price[turn]
            price[turn] = int(c_price) + int(money)
            print('your balance is now:', price[turn],'$')


            


        else:
            print('sorry but you lost! try again.')
            print(roll,'Was the lucky number')
            c_price = price[turn]
            price[turn] = int(c_price) - (int(money) * 0.25)
            print('your balance is now:', price[turn],'$')





        turn += 1
        if turn == len(names):
            turn = 0
        i = input()
        if i == 'exit':
            break
    except:
        print('!!!!!!!!!!!!!!!!!!!!!!')
        print('there went some error')
        print('!!!!!!!!!!!!!!!!!!!!!!')
print('Here are the scores')
try:
    for i in range(len(name)):
        print(names[i],price[i],'$')
except:
    pass


    
    
    

    
    
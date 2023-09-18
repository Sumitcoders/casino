import random
import customtkinter as ctk
import threading
import time

ctk.set_default_color_theme("green")

#player input screen

players = []
balance = []
loan = []
player_list = ''
def add_player():
    global players,player_list
    p = player.get()
    if p != '':
        players.append(p)
        balance.append(100)
        loan.append(0)
        player_list = player_list + p + '\n'
        final_players.configure(text=player_list)
    player.delete(0,len(p))
    print(players)
intake = ctk.CTk()

frame = ctk.CTkFrame(intake,width=int(500),height=int(550))
frame.pack(padx=30,pady=30,expand = True)

lable = ctk.CTkLabel(frame,text='Players',font=('cursive',50))
lable.pack()

player = ctk.CTkEntry(frame,width=420,placeholder_text='name of player')
player.pack(padx = 20,pady=40)


add_button = ctk.CTkButton(frame,text='Add player',command = add_player)
add_button.pack(padx=10,pady=20)

final_players = ctk.CTkLabel(frame,text=player_list,height=200,width=500)
final_players.pack(padx=20,pady=20)

def play():
    global players
    if len(players) == 0:
        pass 
    else:
        intake.destroy()


play = ctk.CTkButton(frame,text='PLAY with these players ▶',command = play)
play.pack(padx=20,pady=20)
intake.mainloop()



#Main screen



root = ctk.CTk()
root.attributes('-fullscreen',True)


frame = ctk.CTkFrame(root,width=900)
frame.pack(padx=30,pady=30)

turn = 0
turn_player = ctk.CTkLabel(frame,text=str('PLAYER: ')+players[turn],font=('Roboto',20))
turn_player.pack(padx=(20,600),pady=20,anchor='w')

turn_balance = ctk.CTkLabel(frame,text=str('BALANCE: ')+str(balance[turn])+'$',font=('Roboto',20))
turn_balance.pack(padx=(20,600),pady=20,anchor='w')

turn_loan = ctk.CTkLabel(frame,text=str('LOAN: ')+str(loan[turn])+'$',font=('Roboto',20))
turn_loan.pack(padx=(20,600),pady=20,anchor='w')
warning = ctk.CTkLabel(root,text='')
warning.pack()
bet = ctk.CTkEntry(root,width =900,height=42,placeholder_text='Enter bet amount',)
bet.pack()

def quarter():
    global balance,turn
    money = balance[turn]/4
    bet.delete(0,'end')
    bet.insert(0,money)

btn_quarter = ctk.CTkButton(root,text='Quarter balance',command=quarter)
btn_quarter.pack(padx=20,pady=20)
btn_quarter.place(x=240,y=360)


def half():
    global balance,turn
    money = balance[turn]/2
    bet.delete(0,'end')
    bet.insert(0,money)

btn_half = ctk.CTkButton(root,text='Half balance',command=half)
btn_half.pack(padx=20,pady=20)
btn_half.place(x=400,y=360)

def three_fourth():
    global balance,turn
    money = balance[turn]*3/4
    bet.delete(0,'end')
    bet.insert(0,money)

btn_full = ctk.CTkButton(root,text='3/4 Balance',command=three_fourth)
btn_full.pack(padx=20,pady=20)
btn_full.place(x=560,y=360)

def full():
    global balance,turn
    money = balance[turn]
    bet.delete(0,'end')
    bet.insert(0,money)

btn_full = ctk.CTkButton(root,text='Full balance',command=full)
btn_full.pack(padx=20,pady=20)
btn_full.place(x=720,y=360)

bet_numbers = []

def disable():
    global check1,check2,check3,check4,check5,check6
    check1.configure(state='disable')
    check2.configure(state='disable')
    check3.configure(state='disable')
    check4.configure(state='disable')
    check5.configure(state='disable')
    check6.configure(state='disable')


def check1_command():
    global check1,bet_numbers
    if check1.state == False:
        check1.state = True
        bet_numbers.append(1)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(1)
        print(bet_numbers)
        check1.state = False

def check2_command():
    global check2,bet_numbers
    if check2.state == False:
        check2.state = True
        bet_numbers.append(2)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(2)
        print(bet_numbers)
        check2.state = False

def check3_command():
    global check3,bet_numbers
    if check3.state == False:
        check3.state = True
        bet_numbers.append(3)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(3)
        print(bet_numbers)
        check3.state = False

def check4_command():
    global check4,bet_numbers
    if check4.state == False:
        check4.state = True
        bet_numbers.append(4)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(4)
        print(bet_numbers)
        check4.state = False
def check5_command():
    global check5,bet_numbers
    if check5.state == False:
        check5.state = True
        bet_numbers.append(5)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(5)
        print(bet_numbers)
        check5.state = False

def check6_command():
    global check6,bet_numbers
    if check6.state == False:
        check6.state = True
        bet_numbers.append(6)
        print(bet_numbers)
        if len(bet_numbers) == 2:
            disable()
    else:
        bet_numbers.remove(6)
        print(bet_numbers)
        check6.state = False

frame1 = ctk.CTkFrame(root,width= 20,height=50)
frame1.pack(padx=20,pady=20)
frame1.place(x=260,y=450)
check1 = ctk.CTkCheckBox(frame1,text='1',width=20,command = check1_command)
check1.pack(padx=10,pady=10,anchor='c')
check1.state = False

frame2 = ctk.CTkFrame(root,width= 20,height=50)
frame2.pack(padx=20,pady=20)
frame2.place(x=340,y=450)
check2 = ctk.CTkCheckBox(frame2,text='2',width=20,command = check2_command)
check2.pack(padx=10,pady=10,anchor='c')
check2.state = False

frame3 = ctk.CTkFrame(root,width= 20,height=50)
frame3.pack(padx=20,pady=20)
frame3.place(x=420,y=450)
check3 = ctk.CTkCheckBox(frame3,text='3',width=20,command = check3_command)
check3.pack(padx=10,pady=10,anchor='c')
check3.state = False

frame4 = ctk.CTkFrame(root,width= 20,height=50)
frame4.pack(padx=20,pady=20)
frame4.place(x=500,y=450)
check4 = ctk.CTkCheckBox(frame4,text='4',width=20,command = check4_command)
check4.pack(padx=10,pady=10,anchor='c')
check4.state = False

frame5 = ctk.CTkFrame(root,width= 20,height=50)
frame5.pack(padx=20,pady=20)
frame5.place(x=580,y=450)
check5 = ctk.CTkCheckBox(frame5,text='5',width=20,command = check5_command)
check5.pack(padx=10,pady=10,anchor='c')
check5.state = False

frame6 = ctk.CTkFrame(root,width= 20,height=50)
frame6.pack(padx=20,pady=20)
frame6.place(x=660,y=450)
check6 = ctk.CTkCheckBox(frame6,text='6',width=20,command = check6_command)
check6.pack(padx=10,pady=10,anchor='c')
check6.state = False

def deselect_all_check():
    global bet_numbers
    check1.deselect()
    check2.deselect()
    check3.deselect()
    check4.deselect()
    check5.deselect()
    check6.deselect()

    check1.configure(state='normal')
    check2.configure(state='normal')
    check3.configure(state='normal')
    check4.configure(state='normal')
    check5.configure(state='normal')
    check6.configure(state='normal')

    check1.state = False
    check2.state = False
    check3.state = False
    check4.state = False
    check5.state = False
    check6.state = False


    bet_numbers = []

deselect = ctk.CTkButton(root,text='Deselect All',command=deselect_all_check)
deselect.place(x=740,y=460)

def erase_bet_output():
    time.sleep(2)
    bet_output.configure(text='' )
    
def player_switch():
    global turn
    turn = turn + 1
    if turn == len(players):
        turn = 0
    
    turn_player.configure(text='PLAYER: '+ players[turn],anchor='w')
    turn_loan.configure(text='LOAN: '+ str(loan[turn]) + '$',anchor='w')
    turn_balance.configure(text='BALANCE:' + str(balance[turn]) + '$',anchor='w')


def bet_bet():
    try:
        float(bet.get()) + 1
    except:
        bet_output.configure(text='Bet not valid')
        t = threading.Thread(target=erase_bet_output)
        t.start()
        bet.delete(0,'end')
        return
    if len(bet_numbers) == 0:
        bet_output.configure(text='No numbers selected')
    elif bet.get() == '' or float(bet.get()) <= 0:
        bet_output.configure(text='Bet not valid')
    elif float(bet.get()) > float(balance[turn]):
        bet_output.configure(text='Not enough Balance')
         
    else:

        a = random.randint(1,6)
        b = random.randint(1,6)
        if b is a:
            b = a +1
            if b > 6:
                b = b - 2
        if a in bet_numbers or b in bet_numbers:
            print('You won the bet')
            bet_output.configure(text='You won the bet')
            print(a,b)
            print(bet_numbers)
            balance[turn] = float(balance[turn]) + float(bet.get()) + float(bet.get()) * 0.5 
            print(balance[turn])
            player_switch()

        else:
            print('loss')
            bet_output.configure(text='You lost the bet')
            balance[turn] = float(balance[turn]) - float(bet.get())
            print(a,b)
            print(bet_numbers)
            player_switch()
        deselect_all_check()
    t = threading.Thread(target=erase_bet_output)
    t.start()
    bet.delete(0,'end')
    #money adding /substracting


    


bet_btn = ctk.CTkButton(root,text='Bet Now!',command= bet_bet)
bet_btn.place(x=260,y=500)

bet_output = ctk.CTkLabel(root,text='',font=('roboto',30))
bet_output.place(x=260,y=550)

frame_loan = ctk.CTkFrame(root)
frame_loan.pack(padx = 30,pady = 20)
frame_loan.place(relx=0.8,rely=0.04)

loan_entry = ctk.CTkEntry(frame_loan,placeholder_text='Enter loan amount')
loan_entry.pack(padx=10,pady=10)

def loan_grant():
    if float(loan_entry.get()) < 0:
        loan_entry.delete(0,'end')
        a = float(loan_entry.get()) * -1
        loan_entry.insert(0,a)
    if balance[turn] <= 0:
        if float(loan_entry.get()) > 100:
            bet_output.configure(text="Can't provide loan more than 100$")
            t = threading.Thread(target=erase_bet_output)
            t.start()
            return
        loan[turn] = float(loan[turn]) + float(loan_entry.get())
        balance[turn] = float(balance[turn]) + float(loan_entry.get())
        turn_loan.configure(text='LOAN: '+ str(loan[turn]) + '$',anchor='w')
        turn_balance.configure(text='BALANCE: '+ str(balance[turn]) + '$',anchor='w')
    else:
        bet_output.configure(text="You have some money left")
        t = threading.Thread(target=erase_bet_output)
        t.start()

loan_btn = ctk.CTkButton(frame_loan,text='Get loan',command=loan_grant)
loan_btn.pack(padx=10,pady=10)

def std_loan():
    if balance[turn] <= 0:

        loan[turn] = float(loan[turn] + 100)
        balance[turn] = float(balance[turn] + 100)
        turn_loan.configure(text='LOAN: '+ str(loan[turn]) + '$',anchor='w')
        turn_balance.configure(text='BALANCE: '+ str(balance[turn]) + '$',anchor='w')
    else:
        bet_output.configure(text="You have some money left")
        t = threading.Thread(target=erase_bet_output)
        t.start()
std_loan_btn = ctk.CTkButton(frame_loan,text='STD. loan',command=std_loan)
std_loan_btn.pack(padx=10,pady=10)

def pay_loan():
    if float(loan_entry.get()) < 0:
        a = loan_entry.get() * -1
        loan_entry.delete(0,'end')
        loan_entry.insert(0,a)
    if float(loan_entry.get()) > loan[turn]:
        a = float(loan[turn])
        loan[turn] = float(loan[turn] - a)
        balance[turn] = float(balance[turn]) - a
        
        turn_loan.configure(text='LOAN: '+ str(loan[turn]) + '$',anchor='w')
        turn_balance.configure(text='BALANCE: '+ str(balance[turn]) + '$',anchor='w')
        return

    if float(loan_entry.get()) > balance[turn]:
        bet_output.configure(text="Not enough balance")
        t = threading.Thread(target=erase_bet_output)
        t.start()
        return
    loan[turn] = float(loan[turn] - float(loan_entry.get()))
    balance[turn] = float(balance[turn]) - float(loan_entry.get())
    turn_loan.configure(text='LOAN: '+ str(loan[turn]) + '$',anchor='w')
    turn_balance.configure(text='BALANCE: '+ str(balance[turn]) + '$',anchor='w')
pay_loan_btn = ctk.CTkButton(frame_loan,text='Pay loan',command=pay_loan)
pay_loan_btn.pack(padx=10,pady=10)

exit_btn = ctk.CTkButton(master=root,command=root.destroy,text='exit')
exit_btn.place(relx=0.89,rely=0.95)


root.mainloop()
    


# winners screen 


def winner_finder():
    i = 0
        
    winner = 'N.A'
    second = 'N.A'
    third = 'N.A'
    winner_bal = 0
    second_bal = 0
    third_bal = 0
    while i < len(players):
            

        if int(balance[i]) >= int(winner_bal):
            third = second
            second = winner
            winner = players[i]
            third_bal = second_bal
            second_bal = winner_bal
            winner_bal = balance[i]
        
        elif int(balance[i]) >= int(second_bal):
            third = second
            second = players[i]
            third_bal = second_bal
            second_bal = balance[i]
        elif int(balance[i]) >= int(third_bal):
            third = players[i]
            third_bal = balance[i]

        i +=1
 
    return winner,second,third                

                
first,second,third = winner_finder() 

winner = ctk.CTk()


frame = ctk.CTkFrame(winner,width = 400)
frame.pack(padx=30,pady=30)
win_lable = ctk.CTkLabel(frame,text="Winners",font=('Cursive',70))
win_lable.pack(padx=30,pady=30)
first_lable = ctk.CTkLabel(frame,text=str("1.")+first,font=('Cursive',50))
first_lable.pack(padx=30,pady=30)
second_lable = ctk.CTkLabel(frame,text=str("2.")+second,font=('Roboto',50))
second_lable.pack(padx=30,pady=30)
third_lable = ctk.CTkLabel(frame,text=str("3.")+third,font=('Cursive',50))
third_lable.pack(padx=30,pady=30)






winner.mainloop()
















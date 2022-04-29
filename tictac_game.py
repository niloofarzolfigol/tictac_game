import os
my_list = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 0]


def print_table(my_list):
    table = f"""
    \t\t     |     |     
    \t\t  {my_list[7]}  |  {my_list[8]}  |  {my_list[9]}  
    \t\t_____|_____|_____
    \t\t     |     |     
    \t\t  {my_list[4]}  |  {my_list[5]}  |  {my_list[6]}  
    \t\t_____|_____|_____
    \t\t     |     |     
    \t\t  {my_list[1]}  |  {my_list[2]}  |  {my_list[3]}  
    \t\t     |     |     
    """
    print(table)


def intro():
    os.system('cls')
    my_main_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('='*90)
    print('\tWelcom to Tic Tac Game.')
    print('\tThis is the number panel for the game.')
    print('\tEach player picks a number until winning by occypying a column, row, or diagonal.')
    print('\tLet\'s start the game!')
    print_table(my_main_list)
    print('='*90)


def print_result(player1_score, player2_score):
    print(f'Player1: {player1_score} \tPlayer2: {player2_score}')
    print('-'*70)
    
    
def choose_X_or_O():
    while True:
        symbol1 = input('Player 1, do you want X or O ? ')
        if symbol1 in ['X', 'x', 'O', 'o']:
            if symbol1 in ['X', 'x']:
                symbol1,symbol2 = 'X','O'
            else:
                symbol1,symbol2 = 'O', 'X'
            return symbol1, symbol2
        else:
            print('Wrong input. Try again. Chose either X or O !')


def check_winner(symbol1, symbol2, my_list):
    if (my_list[1] == my_list[2] == my_list[3] == symbol1) or (my_list[4] == my_list[5] == my_list[6] == symbol1) or (my_list[7] == my_list[8] == my_list[9] == symbol1) or (my_list[1] == my_list[4] == my_list[7] == symbol1) or (my_list[2] == my_list[5] == my_list[8] == symbol1) or (my_list[3] == my_list[6] == my_list[9] == symbol1) or (my_list[1] == my_list[5] == my_list[9] == symbol1) or (my_list[3] == my_list[5] == my_list[7] == symbol1):
        print(f'Player1 ({symbol1}) won!', '\n'+'-'*40)
        return 'Player1'
    if (my_list[1] == my_list[2] == my_list[3] == symbol2) or (my_list[4] == my_list[5] == my_list[6] == symbol2) or (my_list[7] == my_list[8] == my_list[9] == symbol2) or (my_list[1] == my_list[4] == my_list[7] == symbol2) or (my_list[2] == my_list[5] == my_list[8] == symbol2) or (my_list[3] == my_list[6] == my_list[9] == symbol2) or (my_list[1] == my_list[5] == my_list[9] == symbol2) or (my_list[3] == my_list[5] == my_list[7] == symbol2):
        print(f'Player2 ({symbol2}) won!', '\n'+'-'*40)
        return 'Player2'


def get_input(player, symbol, my_list):
    condition = True
    while condition:
        user_input = (input(f'{player} ({symbol}):  Enter a number [1,9]: '))
        try:
            isinstance(int(user_input), int)
        except:
            print('Wrong input. Choose a number from 1 to 9 ')
        else:
            if isinstance(int(user_input), int):
                user_input = int(user_input)
                if 1 <= user_input <= 9:
                    for i in range(1, 10):
                        if user_input == i:
                            if my_list[i] == ' ':
                                my_list[i] = symbol
                                condition = False
                            else:
                                print('Wrong cell. Try another one!')
                else:
                    print('Out of range. Enter a number [1,9]')                
            
    print_table(my_list)


# def calc_scores(winner, player1_score, player2_score): 
#     if winner in ['Player 1', 'Player 2']:
#         if winner == 'Player 1':
#             player1_score += 1
#         else:
#             player2_score += 1

#         return (player1_score, player2_score)

def main_game(my_list, player1_score, player2_score):
    # print_result(player1_score, player2_score)
    symbol1, symbol2 = choose_X_or_O()
    counter = 0

    while True:
        get_input('Player1', symbol1, my_list)
        counter += 1
        winner = check_winner(symbol1, symbol2, my_list)
        
        # s1, s2 = calc_scores(winner, player1_score, player2_score)
        
        if winner in ['Player1', 'Player2']:
            if winner == 'Player1':
                player1_score += 1
            else:
                player2_score += 1
            print_result(player1_score, player2_score)
            return player1_score, player2_score        
        
        
        if counter == 9:
            print('Tie!')
            print_result(player1_score, player2_score)
            return player1_score, player2_score

        get_input('Player2', symbol2, my_list)
        counter += 1
        winner = check_winner(symbol1, symbol2, my_list)
        
        if winner in ['Player1', 'Player2']:
            if winner == 'Player1':
                player1_score += 1
            else:
                player2_score += 1
            print_result(player1_score, player2_score)
            return player1_score, player2_score


def end():
    message = 'End of the game'
    line_ = ''
    print(f'{line_ :->25}{message : ^20}{line_ :-<25}')
    print('-'*70)


def loop(sc1, sc2):
    num_of_rounds = 1
    player1_score, player2_score = sc1, sc2
    while True:
        again = input('Play again? (y/n): ')
        if again in ['y', 'n']:
            if again == 'y':
                num_of_rounds += 1
                my_empty_list = [0, ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', 0]
                new_sc1, new_sc2 = main_game(my_empty_list, player1_score, player2_score)
                player1_score, player2_score = new_sc1, new_sc2
            else:
                word = ''
                if num_of_rounds != 1:
                    word = 's'
                print(f'\nAfter {num_of_rounds} round{word} of games:')
                print_result(player1_score, player2_score)
                end()
                break
        else:
            print('Wrong input. Try again!')


def run():
    intro()
    sc1, sc2 = main_game(my_list, player1_score=0, player2_score=0)
    loop(sc1, sc2)


run()

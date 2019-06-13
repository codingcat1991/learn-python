"""
井字棋游戏
Author: zhouju
Version: 0.1
Date: 2019-06-12
"""
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def tictactoe_game():
    init_board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
                  'ML': ' ', 'MM': ' ', 'MR': ' ',
                  'BL': ' ', 'BM': ' ', 'BR': ' '}
    begin = True
    while begin:
        cur_board = init_board.copy()
        os.system('cls')
        print_board(cur_board)
        begin = False
        turn = 'x'
        counter = 0
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置:' % turn)
            if cur_board[move] == ' ':
                counter += 1
                cur_board[move] = turn
                turn = 'o' if turn == 'x' else 'x'
            os.system('cls')
            print_board(cur_board)
        choice = input("再玩一局？（yes|no）")
        begin = choice == 'yes'


if __name__ == '__main__':
    tictactoe_game()

"""
双色球选号

"""
# from random import randrange, randint, sample

# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()   

# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     # print('sample:',selected_balls)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     # print('randint:',selected_balls)
#     return selected_balls

# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())

# if __name__ == "__main__":
#     main()

"""
约瑟夫环问题
<幸运的基督徒>: 有 15 个基督徒和非基督徒在海上遇难,为了能让一部分人活下来,不得不将其中 15 个人丢进海里去,
有个人想了一个办法就是大家围成一个圈,由某个开始从 1 报数,报到 9 的人就扔到海里面,他后面的人接着从 1 开始
报数,报到 9 的人继续扔到海里面,直到扔掉 15 个人,由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎
么站的，哪些位置是基督徒哪些位置是非基督徒。
"""
# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
        # index %= 30 # ????????????????????????????????/
#     for person in persons:
#         print('基' if person else '非', end='')


# if __name__ == '__main__':
#     main()

"""
井字棋游戏
"""

import os


def print_board(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('-+-+-')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('-+-+-')
	print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
	init_board = {
		'TL': ' ', 'TM': ' ', 'TR': ' ',
		'ML': ' ', 'MM': ' ', 'MR': ' ',
		'BL': ' ', 'BM': ' ', 'BR': ' '
	}
	begin = True
	while begin:
		curr_board = init_board.copy()
		begin = False
		turn = 'x'
		counter = 0
		os.system('clear')
		print_board(curr_board)
		while counter < 9:
			move = input('轮到%s走棋, 请输入位置: ' % turn)
			if curr_board[move] == ' ':
				counter += 1
				curr_board[move] = turn
				if turn == 'x':
					turn = 'o'
				else:
					turn = 'x'
			os.system('clear')
			print_board(curr_board)
		choice = input('再玩一局?(yes|no)')
		begin = choice == 'yes'


if __name__ == '__main__':
	main()
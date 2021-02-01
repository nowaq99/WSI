# author: Adam Nowakowski

from minimax import minimax
import random as rd
import datetime


class CirclesAndCrosses:
    """Circles and crosses game implementation"""

    def __init__(self, search_depth):
        """
        Game implementation with computer opponent
        :param search_depth: parameter for minimax algorithm
        """

        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.state = {'board': self.board.copy(),
                      'max_move': True,
                      'is_terminal': False}
        self.search_depth = search_depth

    def successor_fun(self, state):
        """
        Function which generates next states of the game
        :param state: the initial state from which next states are generated
        :return: list of next states
        """

        out = list()
        if not state['is_terminal']:
            if state['max_move']:
                sign = 'o'
            else:
                sign = 'x'
            for line in range(3):
                for box in range(3):
                    if state['board'][line][box] == ' ':

                        # creating a new state
                        new_state = state.copy()
                        new_state['board'] = [state['board'][i].copy() for i in range(3)]
                        new_state['board'][line][box] = sign
                        new_state['max_move'] = not state['max_move']

                        # terminal conditions
                        # full board
                        con0 = set(new_state['board'][i][j] for i in range(3) for j in range(3)) == {'x', 'o'}
                        # diagonals
                        con_s1 = set(new_state['board'][i][i] for i in range(3)) == {'x'}
                        con_s2 = set(new_state['board'][i][i] for i in range(3)) == {'o'}
                        con_s3 = set(new_state['board'][2-i][i] for i in range(3)) == {'x'}
                        con_s4 = set(new_state['board'][2-i][i] for i in range(3)) == {'o'}
                        # lines
                        for new_line in range(3):
                            con1 = set(new_state['board'][new_line]) == {'x'}
                            con2 = set(new_state['board'][new_line]) == {'o'}
                            con3 = set(new_state['board'][i][new_line] for i in range(3)) == {'x'}
                            con4 = set(new_state['board'][i][new_line] for i in range(3)) == {'o'}
                            if con1 or con3:
                                new_state['is_terminal'] = True
                                new_state['payment'] = -10
                                new_state['end'] = 'x'
                            elif con2 or con4:
                                new_state['is_terminal'] = True
                                new_state['payment'] = 10
                                new_state['end'] = 'o'

                        if (con_s1 or con_s3) and not new_state['is_terminal']:
                            new_state['is_terminal'] = True
                            new_state['payment'] = -10
                            new_state['end'] = 'x'
                        elif (con_s2 or con_s4) and not new_state['is_terminal']:
                            new_state['is_terminal'] = True
                            new_state['payment'] = 10
                            new_state['end'] = 'o'

                        if con0 and not new_state['is_terminal']:
                            new_state['is_terminal'] = True
                            new_state['payment'] = 0
                            new_state['end'] = 'tie'
                        out.append(new_state)
            state['next'] = out
        return out

    def heuristics(self, state):
        """
        heuristics function
        :param state: state from which the heuristics are calculated
        :return: expected payment
        """

        if state['is_terminal']:
            out = state['payment']
        else:
            h_matrix = [[3, 2, 3],
                        [2, 4, 2],
                        [3, 2, 3]]
            out = 0
            for line in range(3):
                for box in range(3):
                    if state['board'][line][box] == 'o':
                        out = out + h_matrix[line][box]
                    elif state['board'][line][box] == 'x':
                        out = out - h_matrix[line][box]
        return out

    def player_move(self):
        """
        The player's movement entered via the keyboard. Changes the state of the object.
        """

        move = input('\nWpisz współrzędne miejsca, w którym chcesz\n'
                     'postawić znak w formie "wiersz-kolumna".\n')
        print('\n')
        length = len(move)
        if self.state['max_move']:
            sign = 'o'
        else:
            sign = 'x'
        w1 = length == 3
        w2 = w3 = w4 = False
        if w1:
            w2 = move[0] in {'1', '2', '3'}
            w3 = move[2] in {'1', '2', '3'}
            w4 = move[1] == '-'
        if w1 and w2 and w3 and w4:
            if self.state['board'][int(move[0])-1][int(move[2])-1] == ' ':
                comp = [self.state['board'][i].copy() for i in range(3)]
                comp[int(move[0])-1][int(move[2])-1] = sign
                possible_states = self.successor_fun(self.state)
                possible_boards = [possible_state['board'] for possible_state in possible_states]
                i = possible_boards.index(comp)
                self.state = possible_states[i]
            else:
                print('\nNie możesz postawić tu znaku!\n')
                self.player_move()
        else:
            print('\nWpisałeś złą wartość!\n')
            self.player_move()

    def opponent_move(self):
        """
        Computer movement - minimax algorithm. Changes the state of the object.
        """

        print('\nKolej przeciwnika.')
        best_payment = minimax(self.state, self.search_depth, self.successor_fun, self.heuristics)
        next_states = self.state['next']
        out_states = list()
        for next_state in next_states:
            if next_state['payment'] == best_payment:
                out_states.append(next_state)
        new_state = rd.choice(out_states)

        self.state = new_state

    def play(self):
        """
        Function to start the game.
        """
        move = rd.choice(('player', 'opponent'))
        move = 'player'
        if move == 'player':
            print('ZACZYNASZ!\n\n')
        while not self.state['is_terminal']:
            print(f'---------------\n'
                  f'{self.state["board"][0]}\n'
                  f'{self.state["board"][1]}\n'
                  f'{self.state["board"][2]}\n'
                  f'---------------\n')

            if move == 'player':
                self.player_move()
                move = 'opponent'
            else:
                self.opponent_move()
                move = 'player'

        print(f'---------------\n'
              f'{self.state["board"][0]}\n'
              f'{self.state["board"][1]}\n'
              f'{self.state["board"][2]}\n'
              f'---------------\n')

        if self.state['end'] == 'o':
            print('WYGRAŁY o!')
        elif self.state['end'] == 'x':
            print('WYGRAŁY x!')
        elif self.state['end'] == 'tie':
            print('REMIS!')


# test

s_depth = 9
a = CirclesAndCrosses(s_depth)
a.play()

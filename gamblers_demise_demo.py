import math
import numpy


def r(capital=100, bet='even'):
    init_capital = capital
    bet_amount = 1
    spin_count = 0
    max_profit = 0

    print ' '
    print 'You start with $100'
    print ' '

    while capital > 0:
        spin_count += 1
        spin_result = numpy.random.randint(0, 37) - 1

        if spin_result == -1:
            spin_result_str = '00'
        else:
            spin_result_str = str(spin_result)

        if spin_result < 1:
            win = False
        if spin_result % 2 == 0:
            if bet == 'even':
                win = True
            if bet == 'odd':
                win = False
        else:
            if bet == 'even':
                win = False
            if bet == 'odd':
                win = True

        if win:
            capital += bet_amount
            bet_amount = 1
        else:
            capital -= bet_amount
            bet_amount *= 2

        if capital - init_capital > max_profit:
            max_profit = capital - init_capital

        print 'Spin ' + str(spin_count) + ": " + spin_result_str.ljust(2) + '     ' + \
              'Bet amount: ' + str(bet_amount).ljust(4) + '     ' + \
              'Total Capital: $' + str(capital)

    print ' '
    print 'You lost in ' + str(spin_count) + ' moves. Your maximum profit was $' + \
          str(max_profit) + '.'


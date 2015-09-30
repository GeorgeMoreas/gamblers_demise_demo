import math
import numpy


def r(capital=1000, bet='even'):
    init_capital = capital
    bet_amount = 10
    spin_count = 0
    max_profit = 0

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
        elif spin_result % 2 == 0:
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
            result = '+ $' + str(bet_amount).ljust(6)
        else:
            capital -= bet_amount
            result = '- $' + str(bet_amount).ljust(6)

        if capital - init_capital > max_profit:
            max_profit = capital - init_capital

        print 'Spin ' + str(spin_count) + ": " + spin_result_str.ljust(6) + \
              'Result: ' + result + \
              'Total Capital: $' + str(capital)

        if win:
            bet_amount = 10
        else:
            bet_amount *= 2

    print ' '
    print 'You started with $1000 and you bet $10 on even, doubling down if you lost.'
    print ' '
    print 'You lost in ' + str(spin_count) + ' moves. Your maximum profit was $' + \
          str(max_profit) + '.'
    print ' '


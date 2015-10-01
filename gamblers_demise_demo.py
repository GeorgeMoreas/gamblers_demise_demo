import math
import numpy


def r(init_cap=1000, bet='even', bet_amount=10, global_turns=1000):
    global_turn_count = 0
    global_max_profit = 0
    global_spin_count = 0
    global_profit_total = 0
    global_profit_avg = 0
    print ' '
    while global_turn_count < global_turns:
        init_capital = init_cap
        spin_count = 0
        max_profit = 0
        capital = init_capital
        global_turn_count += 1
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
            if global_turns == 1:
                print 'Spin ' + str(spin_count) + ": " + spin_result_str.ljust(6) + \
                      'Result: ' + result + \
                      'Total Capital: $' + str(capital)
            if win:
                bet_amount = 10
            else:
                bet_amount *= 2
                if bet_amount > capital:
                    bet_amount = capital
        if global_turns == 1:
            if spin_count == 1:
                moves_str = ' move'
            else:
                moves_str = ' moves'
            print ' '
            print 'You started with $1000 and you bet $10 on even, doubling down if you lost.'
            print ' '
            print 'You lost in ' + str(spin_count) + moves_str + '. Your maximum profit was $' + \
                  str(max_profit) + '.'
            print ' '
        else:
            print 'Round: ' + str(global_turn_count).ljust(8) + \
                  'You lost in ' + str(spin_count).ljust(4) + \
                  ' moves.     Your maximum profit was   $' + \
                  str(max_profit) + '.'

            if global_max_profit < max_profit:
                global_max_profit = max_profit
            global_profit_total += max_profit
            global_spin_count += spin_count
            global_profit_avg = global_profit_total / global_turn_count
            spin_count_avg = global_spin_count / global_turn_count
    if global_turns > 1:
        print ' '
        print 'In ' + str(global_turn_count) + ' rounds, you have averaged $' + \
              str(global_profit_avg) + ' in profit, with a largest profit of $' + \
              str(global_max_profit) + ' and an average spin count per round of ' + \
              str(spin_count_avg) + '.'
        print ' '


# author: Adam Nowakowski

import functions as fun
import NewtonMethod as m


def test(solve):
    print('l. iteracji: ' + str(len(solve)))
    print('wynik:\n' + str(solve[-1]) + '\n')


f1 = m.NewtonMethod(fun.Fun1)
f2 = m.NewtonMethod(fun.Fun2)

test(f1.solve([-10, 0.1], -0.01))
test(f1.solve([-10], -1.1))
test(f2.solve([-10], -0.1))
test(f2.solve([200], -0.7))

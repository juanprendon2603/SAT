from implementacion import reductor, aumentar
from imprimir import imprimir
import sys


def main():

    variables = 0
    clausulas = 0
    SAT = []
    satfile = open(str(sys.argv[1]), 'r').readlines()
    x = int(sys.argv[2])

    for line in satfile:
        if line[0:5] == 'p cnf':
            b = line.split(' ')
            variables = int(b[2])
            clausulas = int(b[3])
        elif line[0] != 'c':
            l = line.split(' ')
            c = [int(l[e]) for e in range(len(l) - 1)]
            SAT.append(c)

    (xsat, clausulas, variables) = reductor(SAT, clausulas, x,
            variables)
    imprimir(xsat, clausulas, variables)


main()

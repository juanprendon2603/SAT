

def aumentar(
    SAT,
    n,
    x,
    variables,
    ):
    lista = []
    for i in range(x - n):
        for j in range(len(SAT)):
            variables += 1
            p = (SAT[j])[:]
            q = (SAT[j])[:]

            p.append(variables)
            lista.append(p)

            q.append(-1 * variables)
            lista.append(q)

        SAT = lista[:]
        lista = []

    return (SAT, variables)


def reductor(
    SAT,
    clausulas,
    x,
    variables,
    ):
    xsat = []
    for clausula in SAT:
        n = len(clausula)
        if x >= n:
            if x >= 3:
                (res, vars_new) = aumentar([clausula], n, x, variables)
            else:
                (res, vars_new) = sat_3sat([clausula], n, x, variables)
        else:
            (res, vars_new) = sat_3sat([clausula], n, x, variables)
        variables = vars_new
        for j in range(len(res)):
            xsat.append(res[j])

    return (xsat, len(xsat), variables)


def sat_3sat(
    SAT,
    n,
    x,
    variables,
    ):
    lista = []
    for clausula in SAT:
        if n == 1:
            lista.append([clausula[0], variables + 1, variables + 2])
            lista.append([clausula[0], variables + 1, -1 * (variables
                         + 2)])
            lista.append([clausula[0], -1 * (variables + 1), variables
                         + 2])
            lista.append([clausula[0], -1 * (variables + 1), -1
                         * (variables + 2)])
            variables += 2
        if n == 2:
            lista.append([clausula[0], clausula[1], variables + 1])
            lista.append([clausula[0], clausula[1], -1 * (variables
                         + 1)])
            variables += 1
        if n == 3:
            lista.append(clausula)
        else:
            lista.append([clausula[0], clausula[1], variables + 1])
            for i in range(2, n - 2):
                lista.append([-1 * (variables + 1), clausula[i],
                             variables + 2])
                variables += 1
            lista.append([-1 * (variables + 1), clausula[n - 2],
                         clausula[n - 1]])
            variables += 1

    return aumentar(lista, 3, x, variables)

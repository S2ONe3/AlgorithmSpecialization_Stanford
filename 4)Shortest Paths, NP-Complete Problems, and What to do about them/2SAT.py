import numpy as np
import pandas as pd
import copy


def isTrue(real_clause, solution):
    clause = copy.deepcopy(real_clause)
    sign = [False] * 2
    if clause[0] < 0:
        clause[0] = -clause[0]
        sign[0] = True
    if clause[1] < 0:
        clause[1] = -clause[1]
        sign[1] = True
    return (sign[0] ^ solution[clause[0] - 1]) or (sign[1] ^ solution[clause[1] - 1])


def satisfied(clauses, solution, n):
    for i in range(n) :
        if isTrue(clauses.iloc[i], solution):
            continue
        else:
            return False
    return True


def change_one_value(caluses, solution, n):
    values_to_be_changed = []
    for clause_idx in range(n):
        if isTrue(clauses.iloc[clause_idx], solution):
            continue
        else:
            if abs(clauses.iloc[clause_idx, 0]) not in values_to_be_changed :
                values_to_be_changed.append(abs(clauses.iloc[clause_idx, 0]))
            if abs(clauses.iloc[clause_idx, 0]) not in values_to_be_changed :
                values_to_be_changed.append(abs(clauses.iloc[clause_idx, 1]))

    if values_to_be_changed:
        values_to_be_changed = list(values_to_be_changed)
        changed_value = values_to_be_changed[np.random.randint(len(values_to_be_changed))] - 1

        solution[changed_value] = not solution[changed_value]
        return True
    else:
        return False


if __name__ == '__main__':

    for filename in ['2sat1.txt', '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']:

        clauses = pd.read_table(filename, sep=' ', names=[0, 1])
        #print(clauses)
        n = len(clauses.index)

        isDone = False

        for _ in range(int(np.log2(n))):
            solution = np.random.randint(0, 2, n, np.bool_)

            for __ in range(2 * n ** 2):
                #print(solution)

                if satisfied(clauses, solution, n):
                    isDone = True
                    break;
                else:
                    if not change_one_value(clauses, solution, n):
                        break

            if isDone:
                break

        if isDone:
            print(1, end='')
        else:
            print(0, end='')

from random import randint
from statistics import mean


class ImpossibleDivideStones(Exception):
    pass


def stones(n: int):
    """
    :param n: number of stones
    :return: tuple of two lists (two heaps with divided stones)
    """

    list_of_stones = []
    for i in range(n):
        list_of_stones.append(randint(0, 1000))

    list_of_stones = sorted(list_of_stones)
    average = mean(sorted(list_of_stones))
    heap1 = []
    heap2 = []

    for elem in list_of_stones:
        if elem < average:
            heap1.append(elem)
        else:
            if sum(list_of_stones[list_of_stones.index(elem):]) / sum(heap1) > 2:
                heap1.append(elem)
                continue
            heap2.append(elem)

    if not heap2:
        raise ImpossibleDivideStones('Error: Impossible to divide the stones into two heaps. '
                                     'The initial weights differ by more than two times')
    return heap1, heap2


decision = stones(10)
if decision:
    print('First heap: ' + str(decision[0]))
    print('Second heap: ' + str(decision[1]))

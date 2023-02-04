import itertools


def permutation(s: str):
    permlist = itertools.permutations(s)
    for i in permlist:
        print("".join(i))

permutation("123")

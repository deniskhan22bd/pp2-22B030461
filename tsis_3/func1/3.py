def solve(numheads: int, numlegs: int):
    animals = dict()
    animals["rabbit"] = (numlegs - 2 * numheads) / 2
    animals["chicken"] = numheads - animals["rabbit"]
    print(animals)

solve(34, 94)
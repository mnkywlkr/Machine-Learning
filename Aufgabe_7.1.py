import itertools

def imright(h1, h2): return h1 - h2 == 1
def nextto(h1, h2): return abs(h1-h2) == 1

def zebra_puzzle_slow():
    houses = [first, _, middle, _, _] = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                for (red, green, ivory, yellow, blue) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, orange_juice, WATER) in orderings
                for (old_gold, kools, chesterfields, parliaments, lucky_striker) in orderings
                if Englishman is red
                if Spaniard is dog
                if coffee is green
                if Ukrainian is tea
                if imright(green,ivory)
                if old_gold is snails
                if kools is yellow
                if milk is middle
                if Norwegian is first
                if nextto(chesterfields, fox)
                if nextto(kools, horse)
                if lucky_striker is orange_juice
                if Japanese is parliaments
                if nextto(Norwegian, blue))

print(zebra_puzzle_slow())

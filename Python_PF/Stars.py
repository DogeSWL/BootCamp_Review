x = [4, 6, 1, 3, 5, 7, 25]

def drawStars(arr):
    for x in arr:
        print "*" * x

# drawStars(x)

g = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw(a,symb):
    return symb * a

def drawStars_v2(arr):
    for x in arr:
        if isinstance(x, int):
            print draw(x,"*")
        elif isinstance(x, str):
            print draw(len(x), (x[0]).lower())


drawStars_v2(g)

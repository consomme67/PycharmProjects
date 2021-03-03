from numpy.random import *

def hoge():
    ran = []
    while len(ran) < 7:
        i = randint(1, 37)
        if not i in ran:
            ran.append(i)
    ran.sort()
    return ran

if __name__ == "__main__":
    j = hoge()
    print(j)
import random

def hoge(s):
    ran = []
    random.seed(s)
    while len(ran) < 7:
        i = random.randint(1, 37)
        if not i in ran:
            ran.append(i)
    ran.sort()
    return ran

if __name__ == "__main__":
    k = input(">>>")

    j = hoge(k)
    print(j)
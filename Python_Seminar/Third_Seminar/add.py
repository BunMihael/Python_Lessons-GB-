def rnd(prev=None):
    if prev is None: prev = int(time())
    rez = (prev * 1103515245 + 12345) % 32767
    return rez

# a0 = int(time())
a1 = rnd()
a2 = rnd(a1)
a3 = rnd(a2)
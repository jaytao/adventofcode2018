f = open('inputs/2','r')

def get_freqs(s):
    a = {}
    for x in s:
        if x not in a:
            a[x] = 1
        else:
            a[x] += 1
    return list(a.values()).count(2), list(a.values()).count(3)

def part1():
    _2 = 0
    _3 = 0
    for x in f:
        _2_count, _3_count = get_freqs(x)
        if _2_count > 0:
            _2 += 1
        if _3_count > 0:
            _3 += 1

    print(_2 * _3)


# generate a unique identifier for a char at an index. abac -> 0*26+0, 1*26+1,2*26+0,3*26+2
def preproc(x):
    l = []
    for c in range(0,len(x)):
        n = c * 26
        n += ord(x[c]) - ord('a')
        l.append(n)
    return l

def part2():
    h = {}
    l = []
    for x in f:
        l.append(x)
    f.close()

    for x in l:
        h[x] = preproc(x)

    for x in l:
        for y in l:
            intersection = [val for val in h[x] if val in h[y]]
            if (len(intersection)) == len(x) - 1:
                print(x)
                print(y)
part2()

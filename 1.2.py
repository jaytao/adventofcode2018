freq = 0
s = set()
while True:
    f = open('1','r')
    for x in f:
        freq += int(x)
        if freq in s:
            print(freq)
            exit()
        s.add(freq)
    f.close()

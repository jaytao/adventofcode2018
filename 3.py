f = open('inputs/3','r')

def parse_line(l):
    _space_split = l.split()
    _top_left = _space_split[2][0:-1].split(',')
    _h_w = _space_split[3].split('x')
    _id = _space_split[0][1:]
    return _id,int(_top_left[0]),int(_top_left[1]),int(_h_w[0]),int(_h_w[1])

def part1_2():
    grid = {}
    grid_ids = {}
    areas = {}
    for x in f:
        _id,x,y,w,h = parse_line(x)
        areas[_id] = w * h
        for _x in range(w):
            x_coord = x + _x
            for _y in range(h):
                y_coord = y + _y
                _tup = (x_coord,y_coord)
                if _tup in grid:
                    grid[_tup] += 1
                    grid_ids[_tup] = -1
                else:
                    grid[_tup] = 1
                    grid_ids[_tup] = _id
    overlaps = 0
    for k,v in grid.items():
        if v >= 2:
            overlaps += 1
    a = [key for key, value in grid.items() if value == 1]
    b = [grid_ids[x] for x in a]
    print("Part 1:",overlaps)
    for k,v in areas.items():
        if b.count(k) == v:
            print("Part 3:", k)
            exit()
part1_2()

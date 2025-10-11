def dirReduc(a):
    cardinal_directions = {
        "SOUTH": "NORTH", "NORTH": "SOUTH", "WEST": "EAST", "EAST": "WEST"
    }
    s = []
    for i in a:
        if s and s[-1] == cardinal_directions.get(i):
            s.pop()
        else:
            s.append(i)
    return s
b = input().split()
res = dirReduc(b)
print(res)
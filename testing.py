text_map = list()
with open(f'data/level/0.txt') as f:
    r = [i.split() for i in f.read().split('\n')]
for i in r:
    print(i)
print(r[2][16])
print(len(r[2]), len(r))

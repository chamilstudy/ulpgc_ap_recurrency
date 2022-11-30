from solve import *

first_line = input().split()
from_value = int(first_line[0])
to_value   = int(first_line[1])
step       = int(first_line[2])

for i in range(from_value, to_value+1, step):
    print(solve(i,to_value), end=' ')
print('')
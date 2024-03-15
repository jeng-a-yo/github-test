import numpy as np


list1 = [(1, 2), (3, 4), (4, 6), (5, 8), (7, 5)]
x = [1, 3, 4, 5, 7]
y = [2, 4, 6, 8, 5]
options = [(1, 7), (4, 5), (5, 3), (8, 5), (11, 9)]
all_answer = []

for a in options:
    x.append(a[0])
    y.append(a[1])
    NPx = np.array(x)
    NPy = np.array(y)
    correlation = np.corrcoef(x, y)
    all_answer.append(correlation[0, 1])
    x.pop(-1)
    y.pop(-1)

all_answer = list(map(lambda x: round(x, 2), all_answer))

print(all_answer)
print("({})".format(all_answer.index(max(all_answer)) + 1),
      options[all_answer.index(max(all_answer))])

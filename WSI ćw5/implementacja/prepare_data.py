# author: Adam Nowakowski

import numpy as np

attributes = [('Class', 'i1'),
              ('Alcohol', 'f8'),
              ('Malic acid', 'f8'),
              ('Ash', 'f8'),
              ('Alcalinity of ash', 'f8'),
              ('Magnesium', 'f8'),
              ('Total phenols', 'f8'),
              ('Flavanoids', 'f8'),
              ('Nonflavanoid phenols', 'f8'),
              ('Proanthocyanins', 'f8'),
              ('Color intensity', 'f8'),
              ('Hue', 'f8'),
              ('OD280/OD315 of diluted wines', 'f8'),
              ('Proline', 'f8')]

file = open('wine.data')
raw_data = list()
for line in file.readlines():
    if line.strip():
        raw_data.append(line.strip().split(','))

data = np.zeros(len(raw_data), dtype=attributes)

for i in range(len(raw_data)):
    for j in range(len(raw_data[i])):
        st = raw_data[i][j]
        data[i][j] = float(st)

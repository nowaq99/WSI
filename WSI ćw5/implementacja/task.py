# author: Adam Nowakowski

from naive_Bayes_classifier import Nbc
from prepare_data import attributes, data
from cross_validation import validation
import numpy as np

table = np.zeros((len(attributes)-1, len(attributes)-1))
k = 8
tests = 10

for t in range(tests):
    for i in range(1, len(attributes)):
        for j in range(1, len(attributes)):
            if i > j:
                new_attributes = [attributes[0], attributes[i], attributes[j]]
                new_data = np.zeros(len(data), dtype=new_attributes)
                new_data[attributes[0][0]] = data[attributes[0][0]]
                new_data[attributes[i][0]] = data[attributes[i][0]]
                new_data[attributes[j][0]] = data[attributes[j][0]]
                err = validation(new_data, Nbc, attributes[0][0], k)
                table[i-1][j-1] = table[i-1][j-1] + err/tests

print(table)

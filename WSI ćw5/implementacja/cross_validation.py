# author: Adam Nowakowski

import numpy as np


def validation(data, method_cls, cls, k):
    """
    Cross-validation implementation.
    :param data: data in the form of structured arrays
    :param method_cls: class of classification method
    :param cls: name of the classifier (string)
    :param k: validation parameter
    :return: average error
    """

    np.random.shuffle(data)
    err = 0
    length = len(data)
    for i in range(k):
        train_data = np.append(data[:int(np.floor(i*length/k))], data[int(np.floor((i+1)*length/k)):])
        test_data = data[int(np.floor(i*length/k)):int(np.floor((i+1)*length/k))]
        obj = method_cls()
        obj.train(train_data, cls)
        err = err + obj.test(test_data)/k
    return err

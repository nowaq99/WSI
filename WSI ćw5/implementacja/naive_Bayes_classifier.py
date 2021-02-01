# author: Adam Nowakowski

import numpy as np


class Nbc:
    """Naive Bayes classifier implementation"""

    def __init__(self):
        """Initialization of variables"""

        self.trained = False
        self.classes = list()
        self.lengths = list()
        self.attributes = list()
        self.data = tuple()
        self.cls = None

    def _prepare(self, data, cls):
        """
        A private method that prepares data for analysis
        :param data: data in the form of structured arrays
        :param cls: name of the classifier (string)
        """

        self.trained = True
        self.cls = cls
        self.attributes = list(data.dtype.names)
        self.attributes.remove(self.cls)
        for entity in data:
            if entity[self.cls] in self.classes:
                self.lengths[self.classes.index(entity[self.cls])] += 1
            else:
                self.classes.append(entity[self.cls])
                self.lengths.append(1)
        data_attributes = [('mean', 'f8'),
                           ('variance', 'f8')]
        self.data = np.zeros((len(self.classes), len(self.attributes)), dtype=data_attributes)

    def train(self, data=None, cls='Class'):
        """
        Calculates normal distribution parameters for subsequent probability calculation
        :param data: data in the form of structured arrays
        :param cls: name of the classifier (string)
        :return: training set error
        """

        if not self.trained or data is not None:
            self._prepare(data, cls)

            for entity in data:
                for attribute in self.attributes:
                    cls_index = self.classes.index(entity[self.cls])
                    attribute_index = self.attributes.index(attribute)
                    length = self.lengths[cls_index]
                    self.data[cls_index][attribute_index]['mean'] += entity[attribute] / length

            for entity in data:
                for attribute in self.attributes:
                    cls_index = self.classes.index(entity[self.cls])
                    attribute_index = self.attributes.index(attribute)
                    mean = self.data[cls_index][attribute_index]['mean']
                    length = self.lengths[cls_index]
                    self.data[cls_index][attribute_index]['variance'] += (entity[attribute] - mean)**2 / length

        return self.test(data)

    def answer(self, entity):
        """
        Calculates the model response to a given input.
        :param entity: input parameters in the form of structured array
        :return: response (class)
        """

        probabilities = list()
        for cls in self.classes:
            cls_index = self.classes.index(cls)
            cls_probability = self.lengths[cls_index]/sum(self.lengths)
            p0 = 1
            for attribute in self.attributes:
                attribute_index = self.attributes.index(attribute)
                var = self.data[cls_index][attribute_index]['variance']
                mean = self.data[cls_index][attribute_index]['mean']
                x = entity[attribute]
                p = (1/(np.sqrt(var)*np.sqrt(2*np.pi)))*np.exp((-(x - mean)**2)/(2*var))
                p0 = p0 * p
            probabilities.append(cls_probability*p0)

        return self.classes[probabilities.index(max(probabilities))]

    def test(self, data):
        """
        Calculates the error of a given test set.
        :param data: test set in the form of structured array
        :return: error
        """
        correct = 0
        for entity in data:
            test_out = self.answer(entity)
            out = entity[self.cls]
            if test_out == out:
                correct = correct + 1
        err = 1 - (correct / len(data))

        return err

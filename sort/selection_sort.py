# coding=utf-8
# author: Lan_zhijiang
# description: 选择排序

import sys
sys.path.append("..")
from base.basic_algorithm import BasicAlgorithm

class SelectionSort():

    def __init__(self):

        self.basic_algorithm = BasicAlgorithm()

    def start(self, array, start=0, end=None):

        """
        选择排序
        :param array: 待排序的数组
        :param start: 开始的index
        :param end: 结束的index
        :return: list/tuple
        """
        if type(array) is list or type(array) is tuple:
            if end is None:
                end = len(array)-1
            if end - start > len(array):
                raise Exception("The end point can't bigger than the length of array!")

            for j in range(start, end):
                smallest, where = self.basic_algorithm.get_smallest(array[j:end+1])
                array[j+where] = array[j]
                array[j] = smallest

            return array
        else:
            raise Exception("You can't sort a array but its type is not list or tuple!")


print(SelectionSort().start([8, 9, 7, 6, 11, 17, 10])) # TEST-RESULT: SUCCESSFUL

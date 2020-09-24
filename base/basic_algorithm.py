# coding=utf-8
# author: Lan_zhijiang
# description: 一些基础算法

class BasicAlgorithm():

    def __init__(self):
        pass

    def get_factorial(self, x):
        result = 1
        for i in range(0, x):
            result = result*i
        return result
# coding=utf-8
# author: Lan_zhijiang
# description: 一些基础算法

class BasicAlgorithm():

    def __init__(self):
        pass

    def get_factorial(self, x):

        """
        计算阶乘
        :param x: x!的x (x>0)
        :return int
        """
        if x < 0:
            raise Exception("Input can't small than 0!")
        elif x == 0:
            return 1
        
        result = 1
        for i in range(1, x):
            result*=i
        return result
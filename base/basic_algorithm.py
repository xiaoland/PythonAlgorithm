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
        for i in range(2, x+1):
            result*=i
        return result

    def get_prime_number(self, start, end):  # HAVEN'T TEST YET

        """
        获取某个范围内的所有素数
        :param start: 开始 int
        :param end: 结束 int
        :return: list
        """
        if start < 0 or end < 0:
            raise Exception("You can't let start or end small than 0!")

        start = int(start)
        end = int(end)
        result = []

        for i in range(start, end+1):
            num = 2
            is_ = True
            while num*num <= i:
                if i % num == 0:
                    is_ = False
                    break
                num += 1
            if is_:
                result.append(i)

        return result

    def is_prime_number(self, x):  # HAVEN'T TEST YET

        """
        判断一个数是否是素数
        :param x: 被判断的数 int >0
        :return:
        """
        if x < 0:
            raise Exception("X must large than 0!")

        result = True
        num = 2
        while num*num <= x:
            if x % num == 0:
                result = False
                break
            num += 1

        return result

    def get_full_array(self, end, length=None):  # HAVEN'T TEST YET

        """
        生成全排列（支持组合）
        :param end: 从1到end  即选择范围（自然数）
        :param length: 序列长度（从选择范围中抽几个数生成序列，默认为None，则就生成end长度的序列）
        :return:
        """
        if length is None:
            length = end

        is_appear = []
        result = []
        array = []

        for i in range(0, end):
            array.append(0)

        def dfs(k):

            if k > length:
                result.append(array)
                return
            else:
                for i in range(1, end+1):
                    if i not in is_appear:
                        is_appear.append(i)
                        array[k] = i
                        dfs(k+1)
                        is_appear.remove(i)

        dfs(1)
        return result

    def get_smallest(self, array):

        """
        获取最小的那个数
        :param array: 输入数组
        :return: result, where
        """
        result = array[0]
        where = 0
        for i in range(0, len(array)):
            if array[i] <= result:
                result = array[i]
                where = i

        return result, where


# print(BasicAlgorithm().get_factorial(4)) # -RESULT: Successful
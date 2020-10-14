# coding=utf-8
# author: Lan_zhijiang
# description: 冒泡排序


class BubbleSort():

    def __init__(self):

        pass

    def start(self, array, start=0, end=None):

        """
        开始排序
        time complexity: O(n^2)
        :param array: 要排序的数组
        :param start: 开始的index
        :param end: 结束的index
        :return: list/tuple (depend on what you gave)
        """
        if type(array) is list or type(array) is tuple:
            if end is None:
                end = len(array)-1
            if end - start + 1 > len(array):
                raise Exception("The end point can't bigger than the length of array!")

            for j in range(end, start, -1):
                for i in range(end, start, -1):
                    if array[i] > array[i-1]:
                        temp = array[i]
                        array[i] = array[i-1]
                        array[i-1] = temp

            return array
        else:
            raise Exception("You can't sort a array but its type is not list or tuple!")


# print(BubbleSort().start([8, 9, 7, 6, 11, 17, 10])) # TEST-RESULT: SUCCESSFUL

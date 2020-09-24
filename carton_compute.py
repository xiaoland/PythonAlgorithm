# coding=utf-8
# author: Lan_zhijiang
# description: 康托运算及其逆运算


class CartonCompute():
    
    def __init__(self):
    
        pass

    def get_factorial(self, x):

        """
        计算阶乘
        :param x: x!的x
        :return int
        """
        result = 1
        for i in range(1, x):
            result = result*i
        return result

    def carton_opreation(self, array, length):

        """
        康托展开
        :param array: 序列
        :param length: 序列长度
        :return int
        """
        appear = []
        ans = 0
        for i in range(0, length):
            nac = 0
            for j in range(1, array[i]):
                if j not in appear:
                    nac+=1
            appear.append(array[i])
            ans = ans + nac*self.get_factorial(length-i)
        
        return ans+1

    def inverse_opreation_of_carton(self, index, length):

        """
        康拓展开逆运算
        :param index: 序号
        :param length: 序列长度
        :return list
        """


# print(CartonCompute().carton_opreation([4, 3, 2, 1], 4)) # -RESULT: Successful